class Cor():
    def __init__(self, r, g, b):
        self.r=r
        self.g=g
        self.b=b
    
    def getCor(self):
        return(self.r/255, self.g/255, self.b/255)
