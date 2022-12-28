class InMemory(object):
    def __init__(self):
        self.store = {}

    def Get(self, key):
        if key in self.store:
            return self.store[key]
        return None

    def Set(self, key, value):
        self.store[key] = value
    
    def All(self):
        return dict(self.store)
