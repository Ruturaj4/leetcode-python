# Design a logger system that receive stream of messages along with its
# timestamps, each message should be printed if and only if it is not
# printed in the last 10 seconds.

# Given a message and a timestamp (in seconds granularity), return true if the
# message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.messages:
            if timestamp - self.messages[message] >= 10:
                self.messages[message] = timestamp
                return True
            else:
                return False
        else:
            self.messages[message] = timestamp
            return True
