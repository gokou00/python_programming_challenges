#https://math.stackexchange.com/questions/1143570/given-two-diagonally-opposite-points-of-a-rectangle-how-to-calculate-the-other
def drawRectangle(canvas, rectangle):
    x1 = rectangle[0]
    y1 = rectangle[1]
    y2 = rectangle[2]
    x2 = rectangle[3]
    canvas[x1][y1] = "*"
    canvas[x2][y2] = "*"
    
    print(canvas)
    
    

print(drawRectangle([['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']],[1, 1, 4, 3]))
    