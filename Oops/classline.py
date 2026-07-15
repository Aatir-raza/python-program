from classpoint import point
class line:
  
  def __init__(self,A,B,C):
    self.A=A
    self.B=B
    self.C=C

  def __str__(self):
    return '{}x +{}y+{} =0'.format(self.A,self.B,self.C) 
  
  def point_on_line(line,point):
    if line.A*point.x_cod + line.B*point.y_cod+line.C==0:
      return"lies on the line"
    
    else:
      return"does not lie on the line"
    
L1=line(1,1,-2)
p1=point(1,1)
print(L1)
print(p1)
print(L1.point_on_line(p1))

def shortest_distance(line,point):
  return abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/(line.A**2+line.B**2)**0.5
L1=line(1,1,-2)
p1=point(1,10)
print(L1)
print(p1)

    