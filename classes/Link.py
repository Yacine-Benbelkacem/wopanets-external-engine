from .Node import *

class Link(Node):
    def __init__(self,
                 name="",
                 kind='link',
                 service_policy="",
                 capacity=10,
                 frm="",
                 to="",
                 from_port=0,
                 to_port=0,
                 network=None):
        
        super().__init__(name,kind,service_policy,capacity)
        
        self.__reverse_usage = 0.
        self.__direct_usage = 0.
        self.__from_port = from_port
        self.__to_port = to_port
        self.__frm = frm
        self.__to = to
        self.__reverse_load = 0.
        self.__direct_load = 0.

        
        self.network = network
        #self.network.links.append(self)
        
    # Start of user code -> properties/constructors for Link class

    # End of user code
    def compute_usage(self):
        #  compute_usage function body
        for f in self.network.flows:
            for t in f.targets:
                if (self.__frm in t.path) and (self.__to in t.path):
                    if (t.path.index(self.__frm) < t.path.index(self.__to) ): 
                        self.__direct_usage += (f.payload()+self.network.overhead())*8.0/f.period()
                    else:
                        self.__reverse_usage += (f.payload()+self.network.overhead())*8.0/f.period()
                    break
        
        # End of user code	
    def compute_load(self):
        #  compute_load function body
        self.__direct_load= self.__direct_usage/self.capacity()
        self.__reverse_load= self.__reverse_usage/self.capacity()
        # End of user code	
    def frm(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__frm=args[0]
        else:
            return self.__frm
    
    def to(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__to=args[0]
        else:
            return self.__to	

    def from_port(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__from_port=args[0]
        else:
            return self.__from_port

        
    def to_port(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__to_port=args[0]
        else:
            return self.__to_port
        
    def direct_load(self):
        #  direct_load function body
        return self.__direct_load
        # End of user code	
    def reverse_load(self):
        #  reverse_load function body
        return self.__reverse_load
        # End of user code	
    def direct_usage(self):
        #  direct_usage function body
        return self.__direct_usage
        # End of user code	
    def reverse_usage(self):
        #  reverse_usage function body
        return self.__reverse_usage
        # End of user code	
    # Start of user code -> methods for Link class

    # End of user code

