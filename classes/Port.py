
class Port(object):
    def __init__(self,number=0,device=None,link=None,sense=None):
        self.__device = device
        self.__link = link
        self.__backlog = 0
        self.__number = number
        self.__delay = 0.
        self.__sense=sense

    
    
    
    
    
    def compute_backlog(self):
        # Start of user code protected zone for compute_backlog function body
        self.__backlog=0
        # End of user code	
        
    def compute_delay(self):
        # Start of user code protected zone for compute_delay function body
        if not(self.__device.is_switch()):
            for f in self.__device.flows:
                self.__delay += (f.payload() + f.overhead())*8/self.__device.capacity()
        # End of user code	
        
    def number(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__number=args[0]
        else:
            return self.__number
        # End of user code	
        
    def backlog(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__backlog=args[0]
        else:
            return self.__backlog
        
    def delay(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__delay=args[0]
        else:
            return self.__delay

    def link(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__link=args[0]
        else:
            return self.__link
        
    def device(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__device=args[0]
        else:
            return self.__device