"""Very basic example of using a sprite image to draw a shape more similar 
how you would do it in a real game instead of the simple line drawings used 
by the other examples. 
"""

from demo_lib import *

def main():
    space.gravity = 0, -900
    
    img = pygame.image.load("pymunk_logo.png")
    p0 = 20, 180
    Segment(p0, (400, -40), (0, 100))

    ticks_to_next_spawn = 10
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == KEYDOWN and event.key == K_p:
                pygame.image.save(screen, "using_sprites.png")  
        
        ticks_to_next_spawn -= 1
        if ticks_to_next_spawn <= 0:
            ticks_to_next_spawn = 100

            pos = random.randint(100, 400), 500
            vs = [(-23,26), (23,26), (0,-26)]
            poly = Poly(pos, vs, img)
            poly.body.angle = random.random() * math.pi
       
        ### Update physics
        dt = 1.0/60.0
        for x in range(1):
            space.step(dt)
            
        ### Draw stuff
        screen.fill(BLACK)
        space.debug_draw(draw_options)
           
        for obj in objects:
            obj.draw()

        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption(f'fps: {clock.get_fps():.1f}')
        
if __name__ == '__main__':
    main()