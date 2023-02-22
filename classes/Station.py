from .Node import *
class Station(Node):
    def __init__(self,
                 name="",
                 kind='station',
                 service_policy="",
                 capacity=10,
                 network=None):
        
        super().__init__(name,kind,service_policy,capacity,network)
        
        self.__is_switch=False
        self.__port=None
        self.__link = None
        self.__service_cruve=None
        self.flows = []

    def is_switch(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__is_switch=args[0]
        else:
            return self.__is_switch
    
    def port(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__port=args[0]
        else:
            return self.__port
    
    def link(self,*args):
            # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__link=args[0]
        else:
            return self.__link

    def service_curve(self,*args):
            # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__service_curve=args[0]
        else:
            return self.__service_curve