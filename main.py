import pygame,sys,pymunk

def create_blocks(space):
    body=pygame.body(1,100,body_type=pymunk.Body.DYNAMIC)
    body.position = (300,200)
    shape=pymunk.Poly

pygame.init()
screen=pygame.display.set_mode((600,400))
clock=pygame.time.Clock()
space=pymunk.space()
space.gravity = (0,500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))
    pygame.display.update()
    clock.tick(120)

