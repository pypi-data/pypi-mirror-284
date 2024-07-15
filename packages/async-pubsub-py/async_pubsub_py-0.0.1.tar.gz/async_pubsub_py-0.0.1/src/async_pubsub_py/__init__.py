# SPDX-FileCopyrightText: 2024-present vikyw89 <vikyw89@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Awaitable, Dict, List


class PubSub:
    def __init__(self):
        """
        Initializes the PubSub class instance with an empty dictionary to store subscribers.
        """
        self.subscribers: Dict[str, List[Callable[[str], Awaitable[None]]]] = {}

    async def publish(self, topic: str, message: str) -> None:
        """
        Asynchronously publishes a message to all subscribers of the given topic.
        
        Parameters:
            topic (str): The topic to which the message is being published.
            message (str): The message to be published.
        
        Returns:
            None
        """
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                await subscriber(message)

    def subscribe(self, topic: str, callback: Callable[[str], Awaitable[None]]) -> None:
        """
        Subscribes a callback function to a specific topic.

        Args:
            topic (str): The topic to subscribe to.
            callback (Callable[[str], Awaitable[None]]): The callback function to be called when a message is published to the topic.

        Returns:
            None: This function does not return anything.
        """
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)

    def unsubscribe(
        self, topic: str, callback: Callable[[str], Awaitable[None]]
    ) -> None:
        """
        Unsubscribes a callback function from a specific topic.

        Parameters:
            self: The instance of the PubSub class.
            topic (str): The topic from which to unsubscribe the callback.
            callback (Callable[[str], Awaitable[None]]): The callback function to be unsubscribed.

        Returns:
            None
        """
        if topic in self.subscribers:
            if callback in self.subscribers[topic]:
                self.subscribers[topic].remove(callback)
            if not self.subscribers[topic]:
                del self.subscribers[topic]
