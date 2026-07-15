class point:
  def __init__(self,x,y):
    self.x_cod = x
    self.y_cod = y

  def __str__(self):
    return '<{},{}>'.format (self.x_cod,self.y_cod)
  
  def euclidean_distance(self,other):
    return((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)**0.5
  
  def distance_from_origin(self):
    # return self.euclidean -distance (point(0,0))
    return self.euclidean_distance(point(0,0))
  
p1= point(3,4)
print(p1)
print(p1.distance_from_origin())
   



