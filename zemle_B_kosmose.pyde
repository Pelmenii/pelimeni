x = 0
y = 200
b = 0
c = 0
v = 0
n = 300
def setup():
    size(2000,1000)
def draw():
    global x,c,v,b,y,n
    background(b,c,v)
    
    push()
    translate(1000,700)
    rotate(radians(x))
    
    fill(200,200,200)
    ellipse(600,-200,80,80)
    ellipse(y,200,1,1)
    pop()
    push()
    point(random(5,600),random(5,600))
    stroke(random(0,255),random(0,255),random(0,255))
    strokeWeight(random(10,10))
    pop()
    fill(255,255,0)
    ellipse(1000,50,200,200)
    fill(0,0,204)
    ellipse(1000,500,200,200)
    fill(86, 180, 25)
    ellipse(1000,510,200,179)


    y += 1
    x = x + 1
    if y <= 380:
        b = b + 1
        c = c + 1
        v = v + 2
    if y >= 380:
        b = b - 1
        c = c - 1
        v = v - 2
    if y >= 560:
        y = 200
