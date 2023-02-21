
from .Node import *

class Switch(Node):
    def __init__(self,
                 name="",
                 kind='switch',
                 service_policy="",
                 capacity=10,
                 
                 latency=0,
                 buffer_size=0,
                 network=None):
        
        super().__init__(name,kind,service_policy,capacity)
        
        self.__latency = latency
        self.__backlog = 0
        self.ports = []
        self.__switching_technique = ""
        self.__memory_percent = 0.
        self.links = []
        self.__buffer_size = buffer_size
        
        if (network != None):
            self.network = network
            #self.network.switches.append(self)
        else:
            self.network=None
        
    # Start of user code -> properties/constructors for Switch class

    # End of user code
    def compute_total_backlog(self):
        # Start of user code protected zone for compute_total_backlog function body
        self.__backlog = 0
        # End of user code	
    def compute_memory_percent(self):
        # Start of user code protected zone for compute_memory_percent function body
        self.__memory_percent = 0
        # End of user code	
    def latency(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__latency=args[0]
        else:
            return self.__latency
        # End of user code	
    def backlog(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__backlog=args[0]
        else:
            return self.__backlog
        # End of user code	
    # Start of user code -> methods for Switch class

    # End of user code

