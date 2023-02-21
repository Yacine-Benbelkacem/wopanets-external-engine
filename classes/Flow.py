
class Flow(object):
    def __init__(self,name,source,payload,overhead,period,network):
        self.__priority = ""
        self.__eed = 0.
        self.__overhead = overhead
        self.__name = name
        self.__payload = payload
        self.__jitter = 0.
        self.source = source
        self.targets = []
        self.__deadline = 0.
        self.__period = period
        
        if (network != None):
            self.network = network
            #self.network.flows.append(self)
        else:
            self.network=None
        
    # Start of user code -> properties/constructors for Flow class
	
    def name(self,*args):
        # Start of user code protected zone for name function body
        if len(args) > 0:
            self.__name=args[0]
        else:
            return self.__name
        # End of user code	
    def period(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__period=args[0]
        else:
            return self.__period
        # End of user code	

        # End of user code	
        # End of user code	
    def deadline(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__deadline=args[0]
        else:
            return self.__deadline
        # End of user code	

    def jitter(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__jitter=args[0]
        else:
            return self.__jitter

    def payload(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__payload=args[0]
        else:
            return self.__payload

        # End of user code	
    def priority(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__priority=args[0]
        else:
            return self.__priority
        
    def overhead(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__overhead=args[0]
        else:
            return self.__overhead
        # End of user code	
    # Start of user code -> methods for Flow class

    # End of user code

