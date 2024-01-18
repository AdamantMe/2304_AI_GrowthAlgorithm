class BaseGrowthRule:
    #Consumed by other classes 
    def apply(self, grid):
        raise NotImplementedError("apply method is not implemented")