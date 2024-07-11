import unittest
from unittest.mock import patch, MagicMock
from consumer import RabbitMQConsumer


class TestRabbitMQConsumer(unittest.TestCase):

    @patch('consumer.pika.BlockingConnection')  # type: ignore
    @patch('consumer.pika.ConnectionParameters')  # type: ignore
    @patch('consumer.pika.PlainCredentials')  # type: ignore
    def setUp(self, mock_plain_credentials: MagicMock,
              mock_connection_parameters: MagicMock,
              mock_blocking_connection: MagicMock) -> None:
        self.mock_channel = MagicMock()
        self.mock_connection = MagicMock()
        self.mock_connection.channel.return_value = self.mock_channel
        mock_blocking_connection.return_value = self.mock_connection

        self.rabbitmq_consumer = RabbitMQConsumer()

        mock_plain_credentials.assert_called_with('guest', 'guest')
        mock_connection_parameters.assert_called_with(
            host='localhost',
            port=5672,
            credentials=mock_plain_credentials.return_value,
            heartbeat=600
        )
        mock_blocking_connection.assert_called_with(
            mock_connection_parameters.return_value)

    def test_declare_queue(self) -> None:
        queue_name = 'test_queue'
        self.rabbitmq_consumer.queue = queue_name
        self.rabbitmq_consumer.declare_queue()
        self.mock_channel.queue_declare.assert_called_with(queue=queue_name,
                                                           durable=True)

    def test_start_consuming(self) -> None:
        self.rabbitmq_consumer.start_consuming()
        self.mock_channel.basic_qos.assert_called_with(prefetch_count=1)
        self.mock_channel.basic_consume.assert_called_with(
            queue=self.rabbitmq_consumer.queue,
            on_message_callback=self.rabbitmq_consumer.callback,
            auto_ack=False
        )
        self.mock_channel.start_consuming.assert_called_once()

    def test_callback(self) -> None:
        mock_channel = MagicMock()
        mock_method = MagicMock()
        mock_properties = MagicMock()
        body = b'Test Message'
        mock_method.delivery_tag = 'test_tag'

        with patch.object(self.rabbitmq_consumer,
                          'process_message') as mock_process_message:
            self.rabbitmq_consumer.callback(mock_channel, mock_method,
                                            mock_properties, body)
            mock_process_message.assert_called_with(body)
            mock_channel.basic_ack.assert_called_with(delivery_tag='test_tag')

    def test_process_message(self) -> None:
        body = b'Test Message'
        with patch('builtins.print') as mock_print:
            self.rabbitmq_consumer.process_message(body)
            mock_print.assert_called_with(
                f"Processing message: {body.decode()}")

    def test_close_connection(self) -> None:
        self.rabbitmq_consumer.close_connection()
        self.mock_connection.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
