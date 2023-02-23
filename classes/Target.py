
class Target(object):
    def __init__(self,name,flow,target):
        self.path = []
        self.__name = name
        self.__target=target
        self.flow = flow
        self.__mode = ""
        self.__eed = 0
        

        
    def compute_eed(self):
        self.__eed = 0
        for i in range( len(self.path)-1 ):
            if self.path[i].is_switch():
                for p in self.path[i].ports:
                    if p.is_from_port(self) and p.neighbour_device() in self.path[i:]:
                        self.__eed += p.delay()
            elif (not(self.path[i].is_switch()) ):
                self.__eed += self.path[i].port().delay()
                    
    def name(self,*args):
        if len(args) > 0:
            self.__name=args[0]
        else:
            return self.__name

    def mode(self,*args):
        if len(args) > 0:
            self.__mode=args[0]
        else:
            return self.__mode
        
    def target(self,*args):
        if len(args) > 0:
            self.__target=args[0]
        else:
            return self.__target
    
    def eed(self,*args):
        if len(args) > 0:
            self.__eed=args[0]
        else:
            return self.__eed

        

