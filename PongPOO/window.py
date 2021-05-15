import pygame

class Window:

    def __init__(self, x, y, title):

        pygame.init()

        self.window = pygame.display.set_mode([x, y])
        self.title = pygame.display.set_caption(title)

        self.loop = True

        self.list_obg = []

    def add_obj(self, item):
        self.list_obg.append(item)

    def draw(self):
        pass

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def updates(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()