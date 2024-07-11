```markdown
# my_rabbitmq_package

A Python package for RabbitMQ interactions.

## Installation

You can install the package using pip:

```bash
pip install my-rabbitmq-package==0.1.3
```

## Publisher Usage

```python
from my_rabbitmq_package.publisher import RabbitMQPublisher

# Initialize the publisher
rabbitmq_publisher = RabbitMQPublisher(host='localhost', port=5672, username='guest', password='guest')

# Declare the queue
rabbitmq_publisher.declare_queue('hello')

# Publish a message
message = "Hello, RabbitMQ!"
rabbitmq_publisher.publish_message(message, 'hello')

# Close the connection
rabbitmq_publisher.close_connection()
```

## Consumer Usage

```python
from my_rabbitmq_package.consumer import RabbitMQConsumer
import threading

# Initialize the consumer
rabbitmq_consumer = RabbitMQConsumer(host='localhost', port=5672, username='guest', password='guest')

# Declare the queue
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

# Start consuming messages in a separate thread
consume_thread = threading.Thread(target=rabbitmq_consumer.consume_messages, args=('hello',))
consume_thread.start()
consume_thread.join()

# Close the connection
rabbitmq_consumer.close_connection()
```

## Running Tests

You can run the tests using `pytest`. First, make sure you have `pytest` installed:

```bash
pip install pytest
```

Then, run the tests:

```bash
pytest tests/
```
