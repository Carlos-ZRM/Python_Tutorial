class CA :
    def __init__(self, rule, ring, times):
        self.rule = rule
        self.ring = ring
        self.times = times
        self.data= []
    def setData(self, data):
        self.data = data
        return
    def getData(self):
        return self.data
    def getRing(self):
        return self.ring
    def getTimes (self):
        return self.times
    def getData (self) :
        return self.data