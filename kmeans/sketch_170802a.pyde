width = 1200
height = 600

points = [(PVector(450,434),0),
          (PVector(400,400),0),
          (PVector(315,412),0),
          (PVector(645,170),0),
          (PVector(584,189),0),
          (PVector(605,223),0),
          (PVector(942,532),0),
          (PVector(901,512),0),
          (PVector(872,472),0)]

catgories = [ color(255,0,0), color(0,0,255), color(34,139,34) ]
k = []        

def setup():
    size(width, height)
    stroke(0)
    for i in range(3):
        x = random(width)
        y = random(height)
        k.append(PVector(x,y))
        
    textSize(32)
    assign_clusters()
    
def draw():
    for p in points:
        fill(catgories[p[1]])
        ellipse(p[0].x,p[0].y, 10, 10)
        
    for p in k:
        fill(0,0,0)
        text("X",p.x,p.y, 15, 15)
        
        
def assign_clusters():
    for x_indx, x in enumerate(points):
        min_distance = sys.maxint
        min_category = 0
        
        for idx,centroid in enumerate(k):
           distance = x[0].dist(centroid)
           
           if distance < min_distance:
               min_distance = distance
               min_category = idx
        
        points[x_indx] = (x[0], min_category)