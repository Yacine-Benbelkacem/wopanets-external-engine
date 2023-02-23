
from .Node import *

class Switch(Node):
    def __init__(self,
                 name="",
                 kind='switch',
                 service_policy="",
                 capacity=10,
                 switching_technique="cut_through",
                 latency=0,
                 buffer_size=0,
                 network=None):
        
        super().__init__(name,kind,service_policy,capacity,network)
        
        self.__is_switch=True
        self.__latency = latency #technological latency
        self.__backlog = 0
        self.__switching_technique = switching_technique
        self.__memory_percent = 0.
        self.__buffer_size = buffer_size
        self.links = []
        self.ports = []
        self.flows = []
        
        self.__service_curve = None
        
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
        
    def is_switch(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__is_switch=args[0]
        else:
            return self.__is_switch
        
    def service_curve(self,*args):
            # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__service_curve=args[0]
        else:
            return self.__service_curve
    
    def compute_curves(self):
        for prt in self.ports:
            prt.compute_departure_curve()