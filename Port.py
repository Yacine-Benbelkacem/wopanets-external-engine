
class Port(object):
    def __init__(self):
        self.switch = None
        self.__backlog = 0
        self.__number = 0
        self.__delay = 0.
        
    # Start of user code -> properties/constructors for Port class

    # End of user code
    def compute_backlog(self):
        # Start of user code protected zone for compute_backlog function body
        raise NotImplementedError
        # End of user code	
    def compute_delay(self):
        # Start of user code protected zone for compute_delay function body
        raise NotImplementedError
        # End of user code	
    def number(self):
        # Start of user code protected zone for number function body
        return 0
        # End of user code	
    def number(self, number):
        # Start of user code protected zone for number function body
        raise NotImplementedError
        # End of user code	
    def backlog(self):
        # Start of user code protected zone for backlog function body
        return 0
        # End of user code	
    def backlog(self, number):
        # Start of user code protected zone for backlog function body
        raise NotImplementedError
        # End of user code	
    def delay(self):
        # Start of user code protected zone for delay function body
        return 0.
        # End of user code	
    def delay(self, number):
        # Start of user code protected zone for delay function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Port class

    # End of user code

