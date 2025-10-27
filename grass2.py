from pico2d import load_image

class Grass:
    image = None

    def __init__(self):
        if not Grass.image:
            self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 10)


    def update(self):
        pass
