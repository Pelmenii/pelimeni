def setup():
   size(600,600)
   background(0)
   frameRate(30)
def draw():
   background(0)
   point(random(5,600),random(5,600))
   stroke(random(0,255),random(0,255),random(0,255))
   strokeWeight(random(1,10))
