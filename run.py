# Whack-A-Ghost
# VictorLoren


class Ghost(pygame.sprite.Sprite):
    """A ghost that will born and then escape if her lifespan finishes or dies
    if she is killed.

    Ghost will be associated with a sprite and a physical button. Animations on
    the screen and

    Attributes:
        color: String for the ghost color and referenced by file
            'ghost_COLOR.png'.
        vector: Tuple of two integers to define where the ghost will be located
            on the screen.
        points: Optional integer variable to define the point value rewarded to
            a player's kill.
        isAlive: Boolean to say whether ghost is available to be killed. (False
            when ghost is killed or she escapes.)
    """

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
