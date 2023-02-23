
class Flow(object):
    def __init__(self,name,source,payload,overhead,period,network,jitter=0,deadline=0):
        self.__priority = ""
        self.__overhead = overhead*8
        self.__name = name
        self.__payload = payload*8
        self.__jitter = jitter*0.000001
        self.__deadline = deadline*0.001
        self.__period = period*0.001
        
        self.__rate = (self.__payload+self.__overhead)/(self.__period) #bps      
 
        self.__burst = 2*(self.__payload+self.__overhead) - self.__rate*(self.__period - self.__jitter)# bits
        
        self.source = source
        self.targets = []
        self.network = network
        

    

    def compute_eeds(self):
        for tg in self.targets:
            tg.compute_eed()
             
	
    def name(self,*args):
        if len(args) > 0:
            self.__name=args[0]
        else:
            return self.__name

    def period(self,*args):
        if len(args) > 0:
            self.__period=args[0]
        else:
            return self.__period

    def deadline(self,*args):
        if len(args) > 0:
            self.__deadline=args[0]
        else:
            return self.__deadline

    def jitter(self,*args):
        if len(args) > 0:
            self.__jitter=args[0]
        else:
            return self.__jitter

    def payload(self,*args):
        if len(args) > 0:
            self.__payload=args[0]
        else:
            return self.__payload


    def priority(self,*args):
        if len(args) > 0:
            self.__priority=args[0]
        else:
            return self.__priority
        
    def overhead(self,*args):
        if len(args) > 0:
            self.__overhead=args[0]
        else:
            return self.__overhead

    def rate(self,*args):
        if len(args) > 0:
            self.__rate=args[0]
        else:
            return self.__rate

    def burst(self,*args):
        if len(args) > 0:
            self.__burst=args[0]
        else:
            return self.__burst

