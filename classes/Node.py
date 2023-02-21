class Node(object):
    def __init__(self,name="",kind="",service_policy="",capacity=10):
        self.__name = name
        self.__kind = kind
        self.__service_policy = service_policy
        self.__capacity = capacity
        
    

    
    
    #----------------
    # Getters/setters
    #----------------
    def name(self):
        return self.__name
        	
    def name(self, name):
        self.__name=name
        	
    def kind(self):
        return self.__kind

    def kind(self, kind):        
        self.__kind=kind
        	
    def capacity(self):
        return self.__capacity
        	
    def capacity(self, capacity):
        self.__capacity=capacity
        	
    def service_policy(self):
        return self.__service_policy
        	
    def service_policy(self, service_policy):
        self.__service_policy=service_policy
        	


    

