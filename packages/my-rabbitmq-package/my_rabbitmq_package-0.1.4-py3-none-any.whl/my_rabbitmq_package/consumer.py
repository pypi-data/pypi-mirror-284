import pika  # type: ignore
from pika.adapters.blocking_connection import BlockingChannel  # type: ignore
from typing import Optional, Dict
from event_manager import EventManager  # type: ignore
import tracemalloc
import gc
import threading


class RabbitMQConsumer:
    def __init__(self, host: str = 'localhost', port: int = 5672,
                 username: str = 'guest', password: str = 'guest') -> None:
        self.host: str = host
        self.port: int = port
        self.username = username
        self.password = password
        self.connection: Optional[pika.BlockingConnection] = None
        self.channel: Optional[BlockingChannel] = None
        self.event_manager = EventManager()
        tracemalloc.start()

    def _connect(self) -> None:
        """Establish connection to RabbitMQ server."""
        try:
            credentials = pika.PlainCredentials(self.username, self.password)
            parameters = pika.ConnectionParameters(
                host=self.host,
                port=self.port,
                credentials=credentials,
                heartbeat=600
            )
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Connection error: {e}")
            raise

    def ensure_connection(self) -> None:
        """Ensure that a connection is established."""
        if not self.connection or self.connection.is_closed:
            self._connect()

    def declare_queue(self, queue_name: str = 'hello') -> None:
        """Declare a durable queue."""
        self.ensure_connection()
        try:
            if self.channel:
                self.channel.queue_declare(queue=queue_name, durable=True)
        except pika.exceptions.AMQPError as e:
            print(f"Queue declaration error: {e}")

    def consume_messages(self, queue_name: str = 'hello') -> None:
        """Consume messages from a queue."""
        self.ensure_connection()
        try:
            if self.channel:
                self.channel.basic_consume(
                    queue=queue_name,
                    on_message_callback=self._on_message_received,
                    auto_ack=False)
                print(' [*] Waiting for messages. To exit press CTRL+C')
                self.channel.start_consuming()
        except pika.exceptions.AMQPError as e:
            print(f"Message consumption error: {e}")

    def _on_message_received(self, ch: BlockingChannel,
                             method: pika.spec.Basic.Deliver,
                             properties: pika.spec.BasicProperties,
                             body: bytes) -> None:
        """Internal callback function to process received messages."""
        message = body.decode()
        print(f" [x] Received {message}")

        if message == "STOP":
            print(" [*] Emitting event 'stop_consumer'")
            self.event_manager.emit(event="stop_consumer")
        else:
            # Emit event for further processing
            print(" [*] Emitting event 'message_received'")
            self.event_manager.emit(event="message_received", data=body)
            print(" [*] Event 'message_received' emitted")

        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

        # Monitor memory usage
        self.monitor_memory_usage()

    def monitor_memory_usage(self) -> None:
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        print("[ Top 10 memory usage ]")
        for stat in top_stats[:10]:
            print(stat)

    def monitor_objects(self) -> None:
        gc.collect()
        objs = gc.get_objects()
        types_count: Dict[str, int] = {}
        for obj in objs:
            type_name = type(obj).__name__
            if type_name in types_count:
                types_count[type_name] += 1
            else:
                types_count[type_name] = 1
        print(types_count)

    def close_connection(self) -> None:
        """Close the connection to RabbitMQ server."""
        try:
            if self.connection:
                self.connection.close()
        except pika.exceptions.AMQPError as e:
            print(f"Connection close error: {e}")

    def stop(self) -> None:
        """Stop the consumer gracefully."""
        print(" [*] Stopping consumer")
        if self.channel:
            self.channel.stop_consuming()
        self.close_connection()


# Example usage
if __name__ == "__main__":
    rabbitmq_consumer = RabbitMQConsumer()
    try:
        rabbitmq_consumer.declare_queue('hello')

        # Define event handler functions
        @rabbitmq_consumer.event_manager.on(event="message_received")
        def handle_message_received(data: bytes):
            print(" [*] Event handler 'handle_message_received' triggered")
            print(f"Processing message: {data.decode()}")

        @rabbitmq_consumer.event_manager.on(event="stop_consumer")
        def handle_stop_consumer():
            print(" [*] Event handler 'handle_stop_consumer' triggered")
            rabbitmq_consumer.stop()

        # Start consuming messages in a separate
        # thread to allow for graceful stopping
        consume_thread = threading.Thread(
            target=rabbitmq_consumer.consume_messages, args=('hello',))
        consume_thread.start()
        consume_thread.join()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        rabbitmq_consumer.close_connection()
