
class Target(object):
    def __init__(self,name,flow):
        self.path = []
        self.__name = name
        self.flow = flow
        self.__mode = ""
        
    # Start of user code -> properties/constructors for Target class

    # End of user code
    def name(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__name=args[0]
        else:
            return self.__name
        # End of user code	
    def mode(self,*args):
        # Start of user code protected zone for period function body
        if len(args) > 0:
            self.__mode=args[0]
        else:
            return self.__mode
    # Start of user code -> methods for Target class

    # End of user code

