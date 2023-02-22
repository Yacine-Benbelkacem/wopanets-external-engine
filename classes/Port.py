
from .AffineCurve import *
class Port(object):
    def __init__(self,number=0,device=None,link=None):
        self.__device = device
        self.__link = link
        self.__backlog = 0
        self.__number = number
        self.__delay = 0.
        self.__arrival_curve = None
        self.__departure_curve=None
        self.__arrival_computed = False
        self.__departure_computed = False
    

    
    
    
    def compute_backlog(self):
        # Start of user code protected zone for compute_backlog function body
        self.__backlog=0
        # End of user code	
        
    def compute_delay(self):
        # Start of user code protected zone for compute_delay function body
        # if not(self.__device.is_switch()):
        #     for f in self.__device.flows:
        #         self.__delay += (f.payload() + f.overhead())*8/self.__device.capacity()
        
        # # theorem 1 calculate delay     
        self.__delay = self.__arrival_curve.b()/self.__device.capacity()
        # End of user code	
        
    
    def compute_arrival_curve(self):
        # the arrival curve on one port (in a switch for instance) is
        # the sum of departure curves from external ports passing by this port
        #
        # we have to check the flows in which this port is a from_port, indeed
        # if the current port is a 'from_port' for a flow it means that this flow
        # passes through this port
        #
        # Once we spotted the flows passing through this port we have to retrace
        # the departure curves until the source 
        
        # so now if the current port is a station's port and this station is a source
        # of the current flow  then the arrival_curve is the rate and burst of the flow
        
        arrival = AffineCurve(0,0)
        if not(self.__arrival_computed):
            
            if not(self.__device.is_switch()):
                for f in self.__device.flows:
                    arrival += AffineCurve(f.burst(),f.rate())
            
            
            else: #(if it is a switch)
                for f in self.__device.flows:
                    for tg in f.targets:
                        if self.is_from_port(f): #the port is a dispatcher of the flow 
                            
                            previous_node_index = tg.path.index(self.__device)-1 
                                
                            arrival += tg.path[previous_node_index].compute_departure_curve()
                                
                        break        
        
            self.__arrival_computed = True
            self.__arrival_curve = arrival
            
        return self.__arrival_curve
    
    
    
    def compute_departure_curve(self):
        
        if not(self.__departure_computed):
            if self.__arrival_computed:
                # # theorem 1 calculate delay
                self.compute_delay()
                # theorem 2 delay the arrival curve
                self.__departure_curve = self.__arrival_curve.applyDelay(self.__delay)
                self.__departure_computed = True
                return self.__departure_curve
            
            else:
                self.compute_arrival_curve()
                self.compute_departure_curve()
        
        return self.__departure_curve
    
    def neighbour_device(self):        
        if self.__link.to() == self.__device:
            return self.__link.frm()
        else:
            return self.__link.to()              
                

    def is_from_port(self,tg):
            neighbour = self.neighbour_device()
            if (neighbour in tg.path) and (tg.path.index(self.__device) <  tg.path.index(  neighbour  )) :    
                return True
            else:
                return False
            

    
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