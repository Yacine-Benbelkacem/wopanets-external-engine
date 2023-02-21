from .Node import *
class Station(Node):
    def __init__(self,
                 name="",
                 kind='station',
                 service_policy="",
                 capacity=10,
                 network=None):
        
        super().__init__(name,kind,service_policy,capacity)
        
        if (network != None):
            self.network = network
            #self.network.stations.append(self)
        else:
            self.network=None
        
        self.link = None
        self.flows = []
        
    # Start of user code -> properties/constructors for Station class

    # End of user code
    # Start of user code -> methods for Station class

    # End of user code

