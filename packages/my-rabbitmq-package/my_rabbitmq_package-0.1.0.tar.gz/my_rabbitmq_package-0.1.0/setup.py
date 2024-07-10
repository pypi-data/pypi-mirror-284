from setuptools import setup, find_packages

setup(
    name="my_rabbitmq_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pika",  # Add other dependencies if necessary
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for RabbitMQ interactions",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anshulchaintha/rabbitmqpractice",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
