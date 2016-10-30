

class Ghost(pygame.sprite.Sprite):
    """A ghost that will born and then escape if her lifespan finishes or dies
    if she is killed by player."""

    def __init__(self, color, vector, points=1):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ghost_%s.png' %color)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.points = points
        self.isAlive = False

    def born(self,lifespan):
        self.isAlive = True
        pass

    def escape(self):
        self.isAlive = False
        pass

    def die(self):
        self.isAlive = False
        pass
