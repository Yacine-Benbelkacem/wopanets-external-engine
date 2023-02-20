
class Network(object):
    def __init__(self):
        self.__overhead = 0
        self.__name = ""
        self.links = []
        self.__shortest_path_policy = ""
        self.__technology = ""
        self.flows = []
        self.__capacity = 0.
        self.switches = []
        self.stations = []
        
    # Start of user code -> properties/constructors for Network class

    # End of user code
    def name(self, name):
        # Start of user code protected zone for name function body
        raise NotImplementedError
        # End of user code	
    def name(self):
        # Start of user code protected zone for name function body
        return ""
        # End of user code	
    def overhead(self, name):
        # Start of user code protected zone for overhead function body
        raise NotImplementedError
        # End of user code	
    def overhead(self):
        # Start of user code protected zone for overhead function body
        return 0
        # End of user code	
    def shortest_path_policy(self, name):
        # Start of user code protected zone for shortest_path_policy function body
        raise NotImplementedError
        # End of user code	
    def shortest_path_policy(self):
        # Start of user code protected zone for shortest_path_policy function body
        return ""
        # End of user code	
    def technology(self):
        # Start of user code protected zone for technology function body
        return ""
        # End of user code	
    def technology(self, name):
        # Start of user code protected zone for technology function body
        raise NotImplementedError
        # End of user code	
    def capacity(self):
        # Start of user code protected zone for capacity function body
        return 0.
        # End of user code	
    def capacity(self, name):
        # Start of user code protected zone for capacity function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Network class

    # End of user code

