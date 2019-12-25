"""Very simple breakout clone. A circle shape serves as the paddle, then 
breakable bricks constructed of Poly-shapes. 

The code showcases several pymunk concepts such as elasitcity, impulses, 
constant object speed, joints, collision handlers and post step callbacks.
"""
from demo_lib import *
import random

BALL = 1
BRICK = 2
BOTTOM = 3
PLAYER = 4

class Segment:
    def __init__(self, p, v, d=3):
        self.shape = pymunk.Segment(b0, p, p+v, d)
        self.shape.elasticity = 1 
        space.add(self.shape)

def remove_first(arbiter, space, data):
    shape = arbiter.shapes[0]
    space.remove(shape, shape.body)
    return True

h = space.add_collision_handler(BALL, BOTTOM)
h.begin = remove_first

h = space.add_collision_handler(BRICK, BALL)
h.begin = remove_first

def spawn_bricks():
    for x in range(100, 520, 20):
        for y in range(400, 450, 10):
            body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
            body.position = x, y
            shape = pymunk.Poly.create_box(body, (20,10))
            shape.elasticity = 1.0
            shape.color = BLUE
            shape.group = 1
            shape.collision_type = BRICK
            space.add(body, shape)


def spawn_ball(space, position, direction):
    ball_body = pymunk.Body(1, pymunk.inf)
    ball_body.position = position
    
    ball_shape = pymunk.Circle(ball_body, 5)
    ball_shape.color =  GREEN
    ball_shape.elasticity = 1.0
    ball_shape.collision_type = BALL
    
    ball_body.apply_impulse_at_local_point(Vec2d(direction))
    
    # Keep ball velocity at a static value
    def constant_velocity(body, gravity, damping, dt):
        body.velocity = body.velocity.normalized() * 400
    ball_body.velocity_func = constant_velocity
    
    space.add(ball_body, ball_shape)

def setup_level(space, player_body):
    
    # Remove balls and bricks
    for s in space.shapes[:]:
        if s.body.body_type == pymunk.Body.DYNAMIC and s.body not in [player_body]:
            space.remove(s.body, s)
            
    # Spawn a ball for the player to have something to play with
    spawn_ball(space, player_body.position + (0,40), random.choice([(1,10),(-1,10)]))
    
    # Spawn bricks
    spawn_bricks()

    
def main():
    global space, screen, font, clock

    t1 = Text(f'fps. {clock.get_fps():.1f}', (0, 0)) 
    Text("Move with left/right arrows, space to spawn a ball", (5,height - 35))
    Text("Press R to reset, ESC or Q to quit", (5,height - 20))

    p0 = Vec2d(50, 50)
    p1 = Vec2d(550, 550)
    v0 = Vec2d(500, 0)
    v1 = Vec2d(0, 500)

    Segment(p0, v1)
    Segment(p1, -v0)
    Segment(p1, -v1)

    # bottom - a sensor that removes anything touching it
    bottom = Segment(p0, v0)
    bottom.shape.sensor = True
    bottom.shape.collision_type = BOTTOM
    bottom.shape.color = RED
    
    ### Player ship
    player_body = pymunk.Body(500, pymunk.inf)
    player_body.position = 300,100
    
    player_shape = pymunk.Segment(player_body, (-50,0), (50,0), 8)
    player_shape.color = RED
    player_shape.elasticity = 1.0
    player_shape.collision_type = PLAYER
    
    def pre_solve(arbiter, space, data):
        # We want to update the collision normal to make the bounce direction 
        # dependent of where on the paddle the ball hits. Note that this 
        # calculation isn't perfect, but just a quick example.
        set_ = arbiter.contact_point_set    
        if len(set_.points) > 0:
            player_shape = arbiter.shapes[0]
            width = (player_shape.b - player_shape.a).x
            delta = (player_shape.body.position - set_.points[0].point_a.x).x
            normal = Vec2d(0, 1).rotated(delta / width / 2)
            set_.normal = normal
            set_.points[0].distance = 0
        arbiter.contact_point_set = set_        
        return True
    h = space.add_collision_handler(PLAYER, BALL)
    h.pre_solve = pre_solve
    
    # restrict movement of player to a straigt line 
    move_joint = pymunk.GrooveJoint(space.static_body, player_body, (100,100), (500,100), (0,0))
    space.add(player_body, player_shape, move_joint)

    # Start game
    setup_level(space, player_body)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT: 
                running = False

            elif event.type ==KEYDOWN:
                if event.key in (K_ESCAPE, K_q):
                    running = False
            
                elif event.key == K_p:
                    pygame.image.save(screen, "breakout.png")
                
                elif event.key == K_LEFT:
                    player_body.velocity = (-600,0)
               
                elif event.key == K_RIGHT:
                    player_body.velocity = (600,0)
                
                elif event.key == K_r:
                    setup_level(space, player_body)
            
                elif event.key == K_SPACE:
                    spawn_ball(space, player_body.position + (0,40), random.choice([(1,10),(-1,10)]))

            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_RIGHT):
                    player_body.velocity = 0,0

        t1.set(f'fps. {clock.get_fps():.1f}')

        screen.fill(BLACK)
        space.debug_draw(draw_options)

        for obj in objects:
            obj.draw()
        pygame.display.update()

        clock.tick(fps)
        space.step(1/fps)

    pygame.quit()
        
if __name__ == '__main__':
    main()