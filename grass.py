from pico2d import load_image

class Grass:
    image = None

    def __init__(self, y):
        self.y = y
        if not Grass.image:
            self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, self.y)


    def update(self):
        pass
