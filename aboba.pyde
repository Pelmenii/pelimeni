x=300
z=300
def setup():
    size(600,600)
def draw():
    global x,z
    background(255)
    img=loadImage("332.jpg")
    image(img,300 ,200, x,z )
    x -= 1
    z -= 1
