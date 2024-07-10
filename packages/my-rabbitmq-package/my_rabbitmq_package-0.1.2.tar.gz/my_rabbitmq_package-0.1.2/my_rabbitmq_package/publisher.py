import pika  # type: ignore
from typing import Optional


class RabbitMQPublisher:
    def __init__(self, host: str = 'localhost', port: int = 5672,
                 username: str = 'guest', password: str = 'guest') -> None:
        self.host: str = host
        self.port: int = port
        self.username = username
        self.password = password
        self.connection: Optional[pika.BlockingConnection] = None
        self.channel: Optional[
            pika.adapters.blocking_connection.BlockingChannel] = None

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

    def publish_message(self, message: str, queue_name: str = 'hello') -> None:
        """Publish a message to the specified queue."""
        self.ensure_connection()
        try:
            if self.channel:
                self.channel.basic_publish(
                    exchange='',
                    routing_key=queue_name,
                    body=message,
                    properties=pika.BasicProperties(
                        delivery_mode=2,  # Make message persistent
                    )
                )
                print(f" [x] Sent '{message}'")
        except pika.exceptions.AMQPError as e:
            print(f"Message publish error: {e}")

    def close_connection(self) -> None:
        """Close the connection to RabbitMQ server."""
        try:
            if self.connection:
                self.connection.close()
        except pika.exceptions.AMQPError as e:
            print(f"Connection close error: {e}")


# Example usage
if __name__ == "__main__":
    rabbitmq_publisher = RabbitMQPublisher()
    try:
        rabbitmq_publisher.declare_queue('hello')

        # Publish a message
        message = "STOP"
        rabbitmq_publisher.publish_message(message, 'hello')
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        rabbitmq_publisher.close_connection()
