"""Showcase of a very basic 2d platformer

The red girl sprite is taken from Sithjester's RMXP Resources:
http://untamed.wild-refuge.net/rmxpresources.php?characters

.. note:: The code of this example is a bit messy. If you adapt this to your 
    own code you might want to structure it a bit differently.
"""

from demo_lib import *
import math

def cpfclamp(f, min_, max_):
    """Clamp f between min and max"""
    return min(max(f, min_), max_)

def cpflerpconst(f1, f2, d):
    """Linearly interpolate from f1 to f2 by no more than d."""
    return f1 + cpfclamp(f2 - f1, -d, d)

PLAYER_VELOCITY = 100. * 2.
PLAYER_GROUND_ACCEL_TIME = 0.05
PLAYER_GROUND_ACCEL = (PLAYER_VELOCITY/PLAYER_GROUND_ACCEL_TIME)

PLAYER_AIR_ACCEL_TIME = 0.25
PLAYER_AIR_ACCEL = (PLAYER_VELOCITY/PLAYER_AIR_ACCEL_TIME)

JUMP_HEIGHT = 16. * 3
JUMP_BOOST_HEIGHT = 24.
JUMP_CUTOFF_VELOCITY = 100
FALL_VELOCITY = 250.

JUMP_LENIENCY = 0.05
HEAD_FRICTION = 0.7
PLATFORM_SPEED = 1

class MovingPlatform:
    def __init__(self, path, d=50):
        self.path = path
        self.index = 1
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = self.path[0]
        self.destination = self.path[1]
        self.dir = (Vec2d(self.path[1]) - self.path[0]).normalized()
        self.dx = PLATFORM_SPEED
        shape = pymunk.Segment(self.body, (-d//2, 0), (d//2, 0), 5)
        shape.friction = 1.
        shape.group = 1
        shape.color = BLUE
        space.add(shape)

    def update(self):
        current = Vec2d(self.body.position)
        distance = current.get_distance(self.destination)
        if distance < self.dx:
            self.index = (self.index + 1) % len(self.path)
            self.destination = self.path[self.index]
            self.dir = (self.destination - current).normalized()
        new = current + self.dir * self.dx
        self.body.position = new
        self.body.velocity = (self.dir * self.dx) / dt

class Player:
    def __init__(self):
        body = pymunk.Body(5, pymunk.inf)
        body.position = 100, 100

        def f(arbiter):
            n = -arbiter.contact_point_set.normal
            if n.y > grounding['normal'].y:
                grounding['normal'] = n
                grounding['penetration'] = -arbiter.contact_point_set.points[0].distance
                grounding['body'] = arbiter.shapes[1].body
                grounding['impulse'] = arbiter.total_impulse
                grounding['position'] = arbiter.contact_point_set.points[0].point_b
        
        body.each_arbiter(f)
        
        head = pymunk.Circle(body, 10, (0, 5))
        head2 = pymunk.Circle(body, 10, (0, 13))
        feet = pymunk.Circle(body, 10, (0, -5))
        # Since we use the debug draw we need to hide these circles. To make it 
        # easy we just set their color to black.
        feet.color = BLACK
        head.color = BLACK
        head2.color = BLACK
        mask = pymunk.ShapeFilter.ALL_MASKS ^ passthrough.filter.categories
        sf = pymunk.ShapeFilter(mask=mask)
        head.filter = sf 
        head2.filter = sf 
        feet.collision_type = 1
        feet.ignore_draw = head.ignore_draw = head2.ignore_draw = True
        
        space.add(body, head, feet, head2)
        direction = 1
        remaining_jumps = 2
        landing = {'p': Vec2d.zero(), 'n': 0}
        frame_number = 0
        
        landed_previous = False


def main():
    sound = pygame.mixer.Sound("sfx.wav")
    # img = pygame.image.load("xmasgirl1.png")
    img = pygame.image.load("arlington.png")
    target_vx = 0
    
    space.gravity = 0,-1000
    # draw_options = pymunk.pygame_util.DrawOptions(screen)

    t1 = Text(f'fps. {clock.get_fps():.1f}', (0, 0)) 
    Text("Move with Left/Right, jump with Up, press again to double jump", (5, height-35))
    Text("Press ESC or Q to quit", (5, height-20))

    # box walls 
    Segment(( 10, 50), (290, 0))
    Segment((300, 50), (25, 0), color=RED)
    Segment((325, 50), (25, 0), color=GREEN)
    Segment((350, 50), (25, 0), color=RED)
    Segment((375, 50), (215, 0), (0, 450), (-580, 0), (0, -450))
    
    # rounded shape
    Segment((450, 50), (20, 10), (20, 20), (10, 20), (0, 50))

    # static platforms
    Segment((170, 50), (100, 100))
    Segment((400, 150), (50, 0))
    Segment((400, 200), (50, 0))
    Segment((220, 200), (80, 0))
    Segment((50, 250), (150, 0))
    Segment((10, 370), (40, -120))
    
    # moving platforms
    mp = MovingPlatform([(450,200),(300,300),(450,400)])
    mp2 = MovingPlatform([(550,100),(500,200),(550,300)])

    # pass-through platform
    passthrough = pymunk.Segment(space.static_body, (270, 100), (320, 100), 5)
    passthrough.color = YELLOW
    passthrough.friction = 1.
    passthrough.collision_type = 2
    passthrough.filter = pymunk.ShapeFilter(categories=0b1000)
    space.add(passthrough)
    
    def passthrough_handler(arbiter, space, data):
        if arbiter.shapes[0].body.velocity.y < 0:
            return True
        else:
            return False
            
    space.add_collision_handler(1,2).begin = passthrough_handler
    
    # player
    body = pymunk.Body(5, pymunk.inf)
    body.position = 100, 100
    
    head = pymunk.Circle(body, 10, (0, 5))
    head2 = pymunk.Circle(body, 10, (0, 13))
    feet = pymunk.Circle(body, 10, (0, -5))
    # Since we use the debug draw we need to hide these circles. To make it 
    # easy we just set their color to black.
    feet.color = BLACK
    head.color = BLACK
    head2.color = BLACK

    mask = pymunk.ShapeFilter.ALL_MASKS ^ passthrough.filter.categories
    sf = pymunk.ShapeFilter(mask=mask)
    head.filter = sf 
    head2.filter = sf 
    feet.collision_type = 1
    feet.ignore_draw = head.ignore_draw = head2.ignore_draw = True
    
    space.add(body, head, feet, head2)
    direction = 1
    remaining_jumps = 2
    landing = {'p': Vec2d.zero(), 'n': 0}
    frame_number = 0
    
    landed_previous = False
    
    running = True
    while running:
        
        grounding = {
            'normal' : Vec2d.zero(),
            'penetration' : Vec2d.zero(),
            'impulse' : Vec2d.zero(),
            'position' : Vec2d.zero(),
            'body' : None
        }
        # find out if player is standing on ground
                
        def f(arbiter):
            n = -arbiter.contact_point_set.normal
            if n.y > grounding['normal'].y:
                grounding['normal'] = n
                grounding['penetration'] = -arbiter.contact_point_set.points[0].distance
                grounding['body'] = arbiter.shapes[1].body
                grounding['impulse'] = arbiter.total_impulse
                grounding['position'] = arbiter.contact_point_set.points[0].point_b
        body.each_arbiter(f)
            
        well_grounded = False
        if grounding['body'] != None and abs(grounding['normal'].x/grounding['normal'].y) < feet.friction:
            well_grounded = True
            remaining_jumps = 2
    
        ground_velocity = Vec2d.zero()
        if well_grounded:
            ground_velocity = grounding['body'].velocity
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key in (K_ESCAPE, K_q):
                    running = False
    
                elif event.key == K_p:
                    pygame.image.save(screen, "platformer.png")

                elif event.key in (K_a, K_LEFT):
                    direction = -1
                    target_vx = -PLAYER_VELOCITY

                elif event.key in (K_d, K_RIGHT):
                    direction = 1
                    target_vx = PLAYER_VELOCITY

                elif event.key in (K_s, K_DOWN):
                    direction = -3
                    
                elif event.key in (K_w, K_UP):
                    if well_grounded or remaining_jumps > 0:                    
                        jump_v = math.sqrt(2.0 * JUMP_HEIGHT * abs(space.gravity.y))
                        impulse = (0, body.mass * (ground_velocity.y+jump_v))
                        body.apply_impulse_at_local_point(impulse)
                        remaining_jumps -= 1
                
            elif event.type == KEYUP:
                target_vx = 0
                if event.key == K_UP:                
                    body.velocity.y = min(body.velocity.y, JUMP_CUTOFF_VELOCITY)
                
        # Target horizontal velocity of player
        
        if body.velocity.x > .01:
            direction = 1
        elif body.velocity.x < -.01:
            direction = -1
            
        feet.surface_velocity = -target_vx, 0

        if grounding['body'] != None:
            feet.friction = -PLAYER_GROUND_ACCEL/space.gravity.y
            head.friction = HEAD_FRICTION
        else:
            feet.friction = 0
            head.friction = 0
        
        # Air control
        if grounding['body'] == None:
            body.velocity = Vec2d(
                cpflerpconst(body.velocity.x, target_vx + ground_velocity.x, PLAYER_AIR_ACCEL*dt),
                body.velocity.y)
        
        body.velocity.y = max(body.velocity.y, -FALL_VELOCITY) # clamp upwards as well?
        
        # Move the moving platform
        mp.update()
        mp2.update()
        
        screen.fill(BLACK)
        space.debug_draw(draw_options)
        
        direction_offset = 48+(1*direction+1)//2 * 48
        if grounding['body'] != None and abs(target_vx) > 1:
            animation_offset = 32 * (frame_number // 8 % 4)
        elif grounding['body'] is None:
            animation_offset = 32*1
        else:
            animation_offset = 32*0
        position = body.position +(-16, 28)
        p = pymunk.pygame_util.to_pygame(position, screen)
        screen.blit(img, p, (animation_offset, direction_offset, 32, 48))

        # Did we land?
        if abs(grounding['impulse'].y) / body.mass > 200 and not landed_previous:
            sound.play()
            landing = {'p': grounding['position'],'n': 15}
            landed_previous = True
        else:
            landed_previous = False
        if landing['n'] > 0:
            p = pymunk.pygame_util.to_pygame(landing['p'], screen)
            pygame.draw.circle(screen, YELLOW, p, 15)
            landing['n'] -= 1
               
        frame_number += 1
        t1.set(f'fps: {clock.get_fps():.1f}. frame: {frame_number}')

        # Helper lines
        for y in range(50, height-50, 50):
            pygame.draw.line(screen, LIGHTGRAY, (10, y), (width-10, y), 1)

        for obj in objects:
            obj.draw()
        pygame.display.update()

        clock.tick(fps)
        space.step(1/fps)

    pygame.quit()

if __name__ == '__main__':
    main()