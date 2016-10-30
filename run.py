# Whack-A-Ghost
# VictorLoren

import pygame
import pygame.locals as pyglocals


FPS = 5  # game has very simple animations and requires only slow refreshes
WINDOWWIDTH = 1920  # game will take up whole screen on decent monitor
WINDOWHEIGHT = 1200

#
BLACK = (0,0,0)

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
        self.image = pygame.image.load('ghost_%s.png' %color)
        self.rect = self.image.get_rect()
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



def main():
    # Initialize a black screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Whack-A-Ghost')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pyglocals.QUIT or (event.type == pyglocals.KEYUP and event.key == pyglocals.K_ESCAPE):
                pygame.quit()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
