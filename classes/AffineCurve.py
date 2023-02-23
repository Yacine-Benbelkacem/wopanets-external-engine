class AffineCurve:
    def __init__(self,b,r):
        self.__b = b
        self.__r = r
        
        
    
    def applyDelay(self,d):
        # a(t+d) = b + r*(t+d) = b + r*d + r*t
        return AffineCurve(self.__b + self.__r*d   ,  self.__r)
        
    #load addition 
    def __add__(self,other):
        if isinstance(other, AffineCurve):
            return AffineCurve(self.__b + other.b(), self.__r + other.r())
        else:
            return AffineCurve(self.__b + other, self.__r)
        
    #----- Setters/Getters -----
    def b(self,*args):
        if len(args)>0:
            self.__b=args[0]
        else:
            return self.__b
    
    def r(self,*args):
        if len(args)>0:
            self.__r=args[0]
        else:
            return self.__r
        