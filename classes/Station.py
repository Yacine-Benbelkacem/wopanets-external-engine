from .Node import *
class Station(Node):
    def __init__(self,
                 name="",
                 kind='station',
                 service_policy="",
                 capacity=10,
                 network=None):
        
        super().__init__(name,kind,service_policy,capacity)
        
        self.__is_switch=False
        
        if (network != None):
            self.network = network
            #self.network.stations.append(self)
        else:
            self.network=None
        
        self.link = None
        self.flows = []

    def is_switch(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__is_switch=args[0]
        else:
            return self.__is_switch