
def function(x: int, y: int, z: int):
    if(x + y == z):
        print("x + y = z")
        return True
    elif(x + y > z):
        print("x + y > z")
        return False
    elif(x + y < z):
        print("x + y > z")
        return False

function(10,10,30)
function(5,2,1)
function(1,1,2)