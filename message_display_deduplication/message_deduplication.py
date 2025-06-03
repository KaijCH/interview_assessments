class Message:

    """
        this message class is provided as part of descriotion and should not intefere

    """

    def __init__(self, timestamp: int, message: str) -> None:
        self.message = message
        self.timestamp = timestamp
    
    def displays(self) -> list:
        print(self.timestamp, self.message)
        return [self.timestamp, self.message]
    
    def __str__(self):
        return str(self.timestamp) + "," + self.message

class TestBed:

    """
        this testbed class is provided as part of tests and should not interfere
    
    """

    def __init__(self, tests: list, threshold: int):
        self.tests = collections.deque([Message(t[0], t[1]) for t in tests])
        self.threshold = threshold
        
    def continues(self) -> bool:
        return self.tests
    
    def fetch_latest(self) -> Message:
        if not self.continues():
            return Message("", -1)
        return self.tests.popleft()


"""
    implementation goes below in deduplicates()

"""

import collections

def deduplicates(testcase: TestBed) -> list:
    messages = collections.defaultdict(int)
    register = collections.defaultdict(Message)
    timeframe = 0
    visibles = []

    while testcase.continues():
        msg = testcase.fetch_latest()
        if not msg.message: 
            continue
        if msg.message in messages and msg.timestamp <= messages[msg.message]:
            if messages[msg.message] in register:
                register.pop(messages[msg.message])
        else:
            messages[msg.message] = msg.timestamp + testcase.threshold
            register[msg.timestamp + testcase.threshold] = msg
        
        if timeframe in register:
            msg = register[timeframe]
            register.pop(timeframe)
            visibles.append(msg.displays())
        timeframe += 1
    
    while register:
        if timeframe in register:
            msg = register[timeframe]
            visibles.append(msg.displays())
            register.pop(timeframe)
        timeframe += 1
    
    return visibles
