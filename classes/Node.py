class Node(object):
    def __init__(self,name="",kind="",service_policy="",capacity=10,network=None):
        self.__name = name
        self.__kind = kind
        self.__service_policy = service_policy
        self.__capacity = capacity
        self.network = network    
    

    
    
    #----------------
    # Getters/setters
    #----------------
    def name(self,*args):
        if len(args) > 0:
            self.__name=args[0]
        else:
            return self.__name
        	
    def kind(self,*args):
        if len(args) > 0:
            self.__kind=args[0]
        else:
            return self.__kind
        	
    def capacity(self,*args):
        if len(args) > 0:
            self.__capacity=args[0]
        else:
            return self.__capacity
        	

        	
    def service_policy(self,*args):
        if len(args) > 0:
            self.__service_policy=args[0]
        else:
            return self.__service_policy
        	


    

