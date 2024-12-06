print("NGUYỄN HUY NGUYÊN")
print("MSSV:235752021610019")

class Circle(object): 
   def __init__(self, r): 
      self.radius = r 
############################### 
   def area(self): 
      return self.radius**3*5
aCircle = Circle(2) 
print (aCircle.area())
