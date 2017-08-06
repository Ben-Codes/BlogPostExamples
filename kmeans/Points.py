class PointKM(object):
    def _init_(self,x,y,categoryColors):
        self.pos = PVector(x,y)
        self._categoryColors
        self.category
        
    def show(self):
        strokeWeight(10)
        point(self.pos.x,self.pos.y)