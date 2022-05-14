# kafka

## Ramp up Plan

[What is Kafka](https://developer.confluent.io/what-is-apache-kafka/)

1. [Getting started with Kafka](https://developer.confluent.io/learn-kafka/architecture/get-started/)
1. Use docker compose to create Kafka cluster
   1. `./start-kafka`
1. Connect to kafka
   1. VS Code (From recommended extensions)
   1. UI for Apache Kafka (Already part of local docker-compose.yaml)
1. Create Topics - learn about different options while creating topics
   1. Use extension
   1. Use UI
   1. Use CLI (Hint: exec into broker container)
1. Test cluster using command line
   1. Produce and consume from CLI
   1. Produce from CLI - see the messages in the UI and the VS Code Extension
1. [Create python project](https://developer.confluent.io/get-started/python/#create-project)
   1. Hint: You need to use 3.9
   1. Install `confluent-kafka` with pip
1. Create simple python producer
1. Create simple python consumer
1. Add method to send batch of messages in producer
1. Add method to receive batch of messages in consumer
1. Create at-least once consumer
1. Create at most once consumer
1. Create exactly once consumer using transactions
   1. [Getting started with transactions](https://developer.confluent.io/learn/kafka-transactions-and-guarantees/)
1. Create consumer that handles de-duplication
1. Good to know
   1. [Storage](https://developer.confluent.io/learn/kafka-storage-and-processing/)
   1. [Performance](https://developer.confluent.io/learn/kafka-performance/)
   1. [Testing](https://developer.confluent.io/learn/testing-kafka/)

## Issues

* `confluent-kafka` - No prebuilt wheels for 3.10+
  * https://github.com/confluentinc/confluent-kafka-python/issues/1219
  * https://github.com/confluentinc/confluent-kafka-python/blob/master/INSTALL.md
* `confluent-kafka` - pylint error: Unable to import `confluent_kafka`

## Hacks

```shell
# Repo is automatically installed in editable mode with dev dependencies
# run commands with native executable names
# defined in [console_scripts] section of setup.cfg
producer

# build a package
python -m build

# install the new one in a new virtual environment
PACKAGE="$(pwd)/$(ls dist/*.whl)"
pushd $(mktemp -d)
python -m venv .venv
source .venv/bin/activate
which python # make sure we're under /tmp/tmp.*******
python -m pip install $PACKAGE      # note that all the dependencies (confluent-kafka, fastapi, etc) are pulled in, but the dev dependencies (pytest, pylint) are not

# enjoy your commands!
producer
```
