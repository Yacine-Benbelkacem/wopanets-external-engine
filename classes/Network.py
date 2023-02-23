
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
    def name(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__name=args[0]
        else:
            return self.__name
        

    def overhead(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__overhead=args[0]
        else:
            return self.__overhead
        
    def shortest_path_policy(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__shortest_path_policy=args[0]
        else:
            return self.__shortest_path_policy

    def technology(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__technology=args[0]
        else:
            return self.__technology
        	
    def capacity(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__capacity=args[0]
        else:
            return self.__capacity


    def compute_links_usage(self):
        for l in self.links:
            l.compute_usage()
            
    def compute_links_load(self):
        for l in self.links:
            l.compute_load()
    
    def compute_curves(self):
        for st in self.stations:
            st.compute_curve()
        for sw in self.switches:
            sw.compute_curves()
            
    def compute_flows_delays(self):
        for f in self.flows:
            f.compute_eeds()