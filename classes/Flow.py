
class Flow(object):
    def __init__(self):
        self.__priority = ""
        self.__eed = 0.
        self.__overhead = 0
        self.network = None
        self.__name = ""
        self.__payload = 0.
        self.__jitter = 0.
        self.source = None
        self.targets = []
        self.__deadline = 0.
        self.__period = 0.
        
    # Start of user code -> properties/constructors for Flow class

    # End of user code
    def name(self):
        # Start of user code protected zone for name function body
        return ""
        # End of user code	
    def name(self, name):
        # Start of user code protected zone for name function body
        raise NotImplementedError
        # End of user code	
    def period(self):
        # Start of user code protected zone for period function body
        return 0.
        # End of user code	
    def period(self, period):
        # Start of user code protected zone for period function body
        raise NotImplementedError
        # End of user code	
    def deadline(self):
        # Start of user code protected zone for deadline function body
        return 0.
        # End of user code	
    def deadline(self, period):
        # Start of user code protected zone for deadline function body
        raise NotImplementedError
        # End of user code	
    def jitter(self):
        # Start of user code protected zone for jitter function body
        return 0.
        # End of user code	
    def jitter(self, period):
        # Start of user code protected zone for jitter function body
        raise NotImplementedError
        # End of user code	
    def payload(self):
        # Start of user code protected zone for payload function body
        return 0.
        # End of user code	
    def payload(self, period):
        # Start of user code protected zone for payload function body
        raise NotImplementedError
        # End of user code	
    def priority(self):
        # Start of user code protected zone for priority function body
        return ""
        # End of user code	
    def priority(self, period):
        # Start of user code protected zone for priority function body
        raise NotImplementedError
        # End of user code	
    def overhead(self):
        # Start of user code protected zone for overhead function body
        return 0
        # End of user code	
    def overhead(self, period):
        # Start of user code protected zone for overhead function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Flow class

    # End of user code

