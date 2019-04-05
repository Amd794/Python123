import turtle as t
def tree(length,level):    #树的层次
    if level <= 0:
        return
    t.forward(length)    #前进方向画 length距离
    t.left(45)
    tree(0.6*length,level-1)
    t.right(90)
    tree(0.6*length,level-1)
    t.left(45)
    t.backward(length)
    return
t.pensize(3)
t.color('green')
t.left(90)
tree(100,6)
