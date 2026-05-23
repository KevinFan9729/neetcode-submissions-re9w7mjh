class Logger:

    def __init__(self):
        # we need a hashmap to store the message as the key
        # and the value is time where it is allowed
            # one if the message is new,
            # we populate the hashmap and the value is timestamp + 10 <- when this message is allowed to print again

            # if say the message is old.
            # we check corresponding hashmap value, and compare with the timestamp, if timestamp < value return false
            # if timestamp > value, update value to timestamp + 10 and then return treu
        # Time O(1)
        # space O(n)
        self.messageMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageMap:
            self.messageMap[message] = timestamp+10
            return True
        else:
            if timestamp < self.messageMap[message]:
                return False
            else:
                self.messageMap[message] = timestamp + 10
                return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
