from Node import *

class Link(Node):
    def __init__(self,
                 name="",
                 kind="",
                 service_policy="",
                 capacity=10):
        
        super().__init__(name,kind,service_policy,capacity)
        
        self.__reverse_usage = 0.
        self.__direct_usage = 0.
        self.__from_port = 0
        self.__to_port = 0
        self.__frm = ""
        self.__to = ""
        self.network = None
        self.__reverse_load = 0.
        self.__direct_load = 0.
        self.switches = []
        self.stations = []
        
    # Start of user code -> properties/constructors for Link class

    # End of user code
    def compute_usage(self):
        #  compute_usage function body
        raise NotImplementedError
        # End of user code	
    def compute_load(self):
        #  compute_load function body
        raise NotImplementedError
        # End of user code	
    def frm(self):
        #  from function body
        return ""
        # End of user code	
    def frm(self, frm):
        #  from function body
        raise NotImplementedError
        # End of user code	
    def to(self, to):
        #  to function body
        raise NotImplementedError
        # End of user code	
    def to(self):
        #  to function body
        return ""
        # End of user code	
    def from_port(self):
        #  from_port function body
        return 0
        # End of user code	
    def from_port(self, frm):
        #  from_port function body
        raise NotImplementedError
        # End of user code	
    def to_port(self):
        #  to_port function body
        return 0
        # End of user code	
    def to_port(self, from):
        #  to_port function body
        raise NotImplementedError
        # End of user code	
    def direct_load(self):
        #  direct_load function body
        return 0.
        # End of user code	
    def reverse_load(self):
        #  reverse_load function body
        return 0.
        # End of user code	
    def direct_usage(self):
        #  direct_usage function body
        return 0.
        # End of user code	
    def reverse_usage(self):
        #  reverse_usage function body
        return 0.
        # End of user code	
    # Start of user code -> methods for Link class

    # End of user code

