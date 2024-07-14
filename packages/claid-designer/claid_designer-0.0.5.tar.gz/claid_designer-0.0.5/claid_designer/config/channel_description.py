from dataclasses import dataclass


@dataclass
class ChannelDescription:
    channel_connection: str
    publisher_modules: list
    subscriber_modules: list

