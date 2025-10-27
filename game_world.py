# 게임 내의 객체들의 생성과 소멸을 관리하는 모듈

# world[0] : 1 layer
# world[1] : 2 layer
# world[2] : 3 layer

world = [[], [], []]

def add_object(o, depth = 0):
    world[depth].append(o)

# def add_objects(ol, depth = 0): # add_objects([ball1, ball2])
#     world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise Exception('월드에 존재하지 않는 객체를 삭제하려고 합니다')

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

