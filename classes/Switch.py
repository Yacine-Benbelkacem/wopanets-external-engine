
from Node import *

class Switch(Node):
    def __init__(self):
        self.__latency = 0.
        self.__backlog = 0
        self.ports = []
        self.__switching_technique = ""
        self.network = None
        self.__memory_percent = 0.
        self.links = []
        self.__buffer_size = 0
        
    # Start of user code -> properties/constructors for Switch class

    # End of user code
    def compute_total_backlog(self):
        # Start of user code protected zone for compute_total_backlog function body
        raise NotImplementedError
        # End of user code	
    def compute_memory_percent(self):
        # Start of user code protected zone for compute_memory_percent function body
        raise NotImplementedError
        # End of user code	
    def latency(self):
        # Start of user code protected zone for latency function body
        return 0.
        # End of user code	
    def latency(self, latency):
        # Start of user code protected zone for latency function body
        raise NotImplementedError
        # End of user code	
    def backlog(self):
        # Start of user code protected zone for backlog function body
        return 0
        # End of user code	
    def backlog(self, latency):
        # Start of user code protected zone for backlog function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Switch class

    # End of user code

