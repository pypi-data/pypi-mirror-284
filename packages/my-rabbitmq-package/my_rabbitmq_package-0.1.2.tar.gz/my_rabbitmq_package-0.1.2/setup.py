from setuptools import setup, find_packages  # type: ignore

setup(
    name="my_rabbitmq_package",
    version="0.1.2",
    packages=find_packages(include=["my_rabbitmq_package",
                                    "my_rabbitmq_package.*",
                                    "tests", "tests.*"]),
    install_requires=[
        "pika", "gc", "tracemalloc", "threading"
    ],
    author="Anshul Chaintha",
    author_email="anshulchaintha7@gmail.com",
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
    include_package_data=True,
)
