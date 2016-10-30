# Whack-A-Ghost
# VictorLoren

import pygame
import pygame.locals as pyglocals
import os

FPS = 10  # game has very simple animations and requires only slow refreshes
WINDOWWIDTH = 1600  # game will take up whole screen on decent monitor
WINDOWHEIGHT = 900

#
BLACK = (0,0,0)

class Ghost(pygame.sprite.Sprite):
    '''A ghost that will born and then escape if her lifespan finishes or dies
    if she is killed.

    Ghost will be associated with a sprite and a physical button. Animations on
    the screen and LED button flashes.

    Attributes:
        color: String for the ghost color and referenced by file
            'ghost_COLOR.png'.
        position: Tuple of two integers to define where the ghost will be
            located on the screen.
        points: Optional integer variable to define the point value rewarded to
            a player's kill.
        isAlive: Boolean to say whether ghost is available to be killed. (False
            when ghost is killed or she escapes.)
    '''

    def __init__(self, color, position, points=1):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.image.load(os.path.join('images','ghostLimbo.png'))
        #TODO: Scale image to fit proper screen size
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.position = position  # tuple of integers
        self.points = points
        self.isAlive = False

    def born(self,lifespan):
        self.isAlive = True
        self.image = pygame.image.load(
            os.path.join('images','ghost_%s.png' %self.color))
        print('%s Ghost Born' %self.color)

    def escape(self):
        self.isAlive = False
        self.image = pygame.image.load(
            os.path.join('images','ghostEscape_%s.png' %self.color))
        print('%s Ghost Escaped' %self.color)

    def die(self):
        self.isAlive = False
        self.image = pygame.image.load(
            os.path.join('images','ghostDie.png'))#_%s.png' %self.color))
        print('%s Ghost Died' %self.color)

    def limbo(self):
        '''State of ghost when waiting to be born and therefore invisible to
        the screen.'''

        self.isAlive = False
        self.image = pygame.image.load(os.path.join('images','ghostLimbo.png'))
        print('%s Ghost went to Limbo' %self.color)


def getPosition(x,y):
    '''Defines a vector/position based on the size of the screen.
    Args:
        x: Percent to the right of the screen to define the x-coordinate
        y: Percent to the bottom of the screen to define the y-coordinate
    Returns:
        Tuple of pixels from the top-left corner of the screen
    '''
    return (x*int(WINDOWWIDTH * 0.01), y*int(WINDOWHEIGHT * 0.01))

def main():
    # Initialize a black screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Whack-A-Ghost')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    clock = pygame.time.Clock()
    # Create ghosts
    ghosts = [
        Ghost('white', getPosition(5,15)),
        Ghost('green', getPosition(15,50)),
        Ghost('yellow', getPosition(45,70)),
        Ghost('red', getPosition(65,50)),
        Ghost('blue', getPosition(75,15))
    ]


    while True:
        for event in pygame.event.get():
            if event.type == pyglocals.QUIT or (event.type == pyglocals.KEYUP and event.key == pyglocals.K_ESCAPE):
                pygame.quit()

            #TEST: births
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_1:
                ghosts[0].born(1)
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_2:
                ghosts[1].born(1)
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_3:
                ghosts[2].born(1)
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_4:
                ghosts[3].born(1)
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_5:
                ghosts[4].born(1)
            #TEST: deaths
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_q:
                ghosts[0].die()
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_w:
                ghosts[1].die()
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_e:
                ghosts[2].die()
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_r:
                ghosts[3].die()
            elif event.type == pyglocals.KEYUP and event.key == pyglocals.K_t:
                ghosts[4].die()
        # Update the screen
        clock.tick(FPS)
        screen.fill(BLACK)
        for ghost in ghosts:
            screen.blit(ghost.image, ghost.position)
        pygame.display.update()


if __name__ == '__main__':
    main()
