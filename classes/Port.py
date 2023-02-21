
class Port(object):
    def __init__(self,number=0,device=None,link=None):
        self.__device = device
        self.__link = link
        self.__backlog = 0
        self.__number = number
        self.__delay = 0.

    
    
    
    
    
    def compute_backlog(self):
        # Start of user code protected zone for compute_backlog function body
        self.__backlog=0
        # End of user code	
        
    def compute_delay(self):
        # Start of user code protected zone for compute_delay function body
        self.__delay=0
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