"""Showcase of flying arrows that can stick to objects in a somewhat 
realistic looking way.
"""
from demo_lib import *

space.gravity = 0, -1000

class Poly:
    def __init__(self, pos, vertices):
        self.body = pymunk.Body()
        self.body.position = pos
        shape = pymunk.Poly(self.body, vertices)
        shape.friction = 0.5
        shape.collision_type = 1
        shape.density = 1
        space.add(self.body, shape)

class Arrow(Poly):

    def __init__(self, pos, angle=0):
        vertices = [(-30, 0), (0, 3), (10, 0), (0, -3)]
        super().__init__(pos, vertices)
        self.body.angle = angle


def create_arrow():
    vs = [(-30,0), (0,3), (10,0), (0,-3)]
    mass = 1
    moment = pymunk.moment_for_poly(mass, vs)
    arrow_body = pymunk.Body(mass, moment)

    arrow_shape = pymunk.Poly(arrow_body, vs)
    arrow_shape.friction = .5
    arrow_shape.collision_type = 1
    return arrow_body, arrow_shape
    

def post_solve_arrow_hit(arbiter, space, data):
    if arbiter.total_impulse.length > 300:
        other, arrow = arbiter.shapes
        position = arbiter.contact_point_set.points[0].point_a
        arrow.collision_type = 0
        arrow.group = 1
        # space.add_post_step_callback(
        #     stick_arrow_to_target, arrow.body, other.body, position, data["flying_arrows"])
        pivot_joint = pymunk.PivotJoint(arrow.body, other.body, position)
        phase = other.body.angle - arrow.body.angle 
        gear_joint = pymunk.GearJoint(arrow.body, other.body, phase, 1)
        space.add(pivot_joint, gear_joint)
        try:
            flying_arrows.remove(arrow.body)
        except:
            pass


class Player:
    def __init__(self, pos=(200, 100)):
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.shape = pymunk.Circle(self.body, 25)
        self.shape.sensor = True
        self.shape.color = CYAN
        self.body.position = pos
        self.speed = 2.5
        self.shooting = False
        space.add(self.shape)

    def update(self):
        keys = pygame.key.get_pressed()
        dir = Vec2d(0, 0)
        if (keys[K_a]):
            dir = Vec2d(-1, 0)
        if (keys[K_w]):
            dir = Vec2d(0, 1)
        if (keys[K_s]):
            dir = Vec2d(0, -1)
        if (keys[K_d]):
            dir = Vec2d(1, 0)
        self.body.position += dir * self.speed

        mouse = from_pygame(pygame.mouse.get_pos(), screen)
        self.body.angle = (mouse - self.body.position).angle

    def do_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.shooting = True
            self.t0 = pygame.time.get_ticks()

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.shooting = False
                pos = self.body.position
                arrow = Arrow(pos)
                arrow.body.angle = self.body.angle

                t = pygame.time.get_ticks() - self.t0
                x = min(1000, t) * 100
                impulse = Vec2d(x, 0).rotated(self.body.angle)
                # arrow.body.apply_impulse_at_local_point(impulse)

    def draw(self):
        if self.shooting:
            p = self.body.position
            p0 = to_pygame(p, screen)
            t = pygame.time.get_ticks() - self.t0
            x = min(1000, t) // 10
            p1 = to_pygame(p + Vec2d(x, 0).rotated(self.body.angle), screen)
            pygame.draw.line(screen, RED, p0, p1, 5)


def main():

    t1 = Text(f'fps. {clock.get_fps():.1f}', (0, 0)) 
    Text("Aim with mouse, hold LMB to powerup, release to fire", (5, height - 35))
    Text("Press ESC or Q to quit",  (5, height - 20))

    player = Player()

    # walls - the left-top-right walls
    p0 = 50, 50
    Segment(p0, (500, 0), (0, 500), (-500, 0), (0, -500))

    arrow = Arrow((100, 100))
    
    b2 = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    s2 = pymunk.Circle(b2, 30)
    b2.position = 300,400
    space.add(b2, s2)

    c2 = Circle((200, 200), 30)
    c2.body.body_type = pymunk.Body.KINEMATIC

    # "Cannon" that can fire arrows
    cannon_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    cannon_shape = pymunk.Circle(cannon_body, 25)
    cannon_shape.sensor = True
    cannon_shape.color = (255,50,50)
    cannon_body.position = 100,100
    space.add(cannon_shape)

    arrow_body, arrow_shape = create_arrow()
    space.add(arrow_shape)

    flying_arrows = []    
    handler = space.add_collision_handler(0, 1)
    handler.data["flying_arrows"] = flying_arrows
    handler.post_solve=post_solve_arrow_hit

    t0 = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key in (K_ESCAPE, K_q):
                    running = False

                elif event.key == K_p:
                    pygame.image.save(screen, "arrows.png")

                elif event.key == K_x:
                    a = Arrow((200, 100))
                    a.body.apply_impulse_at_local_point((100000, 0))
                
            elif event.type == KEYUP:
                pass
    
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    t0 = pygame.time.get_ticks()
            
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                
                diff = pygame.time.get_ticks() - t0
                power = max(min(diff, 1000), 10) * 1.5
                impulse = power * Vec2d(1,0)
                impulse.rotate(arrow_body.angle)
                
                arrow_body.apply_impulse_at_world_point(impulse, arrow_body.position)
                
                space.add(arrow_body)
                flying_arrows.append(arrow_body)
                
                arrow_body, arrow_shape = create_arrow()
                space.add(arrow_shape)
            
            player.do_event(event)
        
        player.update()

        keys = pygame.key.get_pressed()
        speed = 2.5
        if (keys[K_UP]):
            cannon_body.position += Vec2d(0,1) * speed
        if (keys[K_DOWN]):
            cannon_body.position += Vec2d(0,-1) * speed
        if (keys[K_LEFT]):
            cannon_body.position += Vec2d(-1,0) * speed
        if (keys[K_RIGHT]):
            cannon_body.position += Vec2d(1,0) * speed

        mouse_position = pymunk.pygame_util.from_pygame( Vec2d(pygame.mouse.get_pos()), screen )
        cannon_body.angle = (mouse_position - cannon_body.position).angle
        # move the unfired arrow together with the cannon
        arrow_body.position = cannon_body.position + Vec2d(cannon_shape.radius + 40, 0).rotated(cannon_body.angle)
        arrow_body.angle = cannon_body.angle
        
        
        for flying_arrow in flying_arrows:
            drag_constant = 0.0002
            
            pointing_direction = Vec2d(1,0).rotated(flying_arrow.angle)
            flight_direction = Vec2d(flying_arrow.velocity)
            flight_speed = flight_direction.normalize_return_length()
            dot = flight_direction.dot(pointing_direction)
            # (1-abs(dot)) can be replaced with (1-dot) to make arrows turn 
            # around even when fired straight up. Might not be as accurate, but 
            # maybe look better.
            drag_force_magnitude = (1-abs(dot)) * flight_speed **2 * drag_constant * flying_arrow.mass
            arrow_tail_position = Vec2d(-50, 0).rotated(flying_arrow.angle)
            flying_arrow.apply_impulse_at_world_point(drag_force_magnitude * -flight_direction, arrow_tail_position)
            
            flying_arrow.angular_velocity *= 0.5
            
        t1.set(f'fps. {clock.get_fps():.1f}')
        screen.fill(BLACK)
        space.debug_draw(draw_options)
        
        # Power meter
        if pygame.mouse.get_pressed()[0]:
            t = pygame.time.get_ticks() - t0
            power = max(min(t, 1000), 10)
            h = power / 2
            pygame.draw.line(screen, RED, (30,550), (30,550-h), 10)
                
        # Info and flip screen
        
        for obj in objects:
            obj.draw()
        player.draw()
        pygame.display.update()

        clock.tick(fps)
        space.step(1/fps)

    pygame.quit()

if __name__ == '__main__':
    main()