import os
import uuid
from dotenv import load_dotenv

load_dotenv()


def base_config():
    config = {
        "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092"),
        # 'debug': 'broker,topic,msg',
    }

    if os.getenv("KAFKA_SASL_MECHANISM") == "PLAIN":
        config = config | {
            "sasl.mechanism": os.getenv("KAFKA_SASL_MECHANISM"),
            "security.protocol": os.getenv("KAFKA_SECURITY_PROTOCOL"),
            "sasl.username": os.getenv("KAFKA_SASL_USERNAME"),
            "sasl.password": os.getenv("KAFKA_SASL_PASSWORD"),
        }

    return config


def producer_config():
    return base_config() | {
        "enable.idempotence": True,
        "acks": "all",
        # 'queue.buffering.max.ms': 500,
        # "batch.num.messages": 1,
    }


def consumer_config():
    return base_config() | {
        "group.id": uuid.uuid1(),
        "auto.offset.reset": "earliest",
        "session.timeout.ms": 6000,
    }
