import unittest
import pika  # type: ignore
from unittest.mock import patch, MagicMock
from publisher import RabbitMQClient  # Importing from publisher module


class TestRabbitMQClient(unittest.TestCase):

    @patch('publisher.pika.BlockingConnection')
    @patch('publisher.pika.ConnectionParameters')
    @patch('publisher.pika.PlainCredentials')
    def setUp(self, mock_plain_credentials, mock_connection_parameters,
              mock_blocking_connection):
        self.mock_channel = MagicMock()
        self.mock_connection = MagicMock()
        self.mock_connection.channel.return_value = self.mock_channel
        mock_blocking_connection.return_value = self.mock_connection

        self.rabbitmq_client = RabbitMQClient()

        mock_plain_credentials.assert_called_with('guest', 'guest')
        mock_connection_parameters.assert_called_with(
            host='localhost',
            port=5672,
            credentials=mock_plain_credentials.return_value,
            heartbeat=600)

        mock_blocking_connection.assert_called_with(
            mock_connection_parameters.return_value)

    def test_declare_queue(self):
        queue_name = 'test_queue'
        self.rabbitmq_client.declare_queue(queue_name)
        self.mock_channel.queue_declare.assert_called_with(queue=queue_name,
                                                           durable=True)

    def test_publish_message(self):
        message = 'Test Message'
        queue_name = 'test_queue'
        self.rabbitmq_client.publish_message(message, queue_name)
        self.mock_channel.basic_publish.assert_called_with(
            exchange='',
            routing_key=queue_name,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )

    def test_close_connection(self):
        self.rabbitmq_client.close_connection()
        self.mock_connection.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
