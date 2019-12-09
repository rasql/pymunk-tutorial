from characters import Pig
from polygon import Polygon, Rectangle


class Level():
    def __init__(self, pigs, columns, beams, space):
        self.pigs = pigs
        self.columns = columns
        self.beams = beams
        self.space = space
        self.number = 0
        self.number_of_birds = 4
        # lower limit
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000
        self.bool_space = False

    def open_flat(self, x, y, n):
        """Create a open flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*100
            p = (x, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+50)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def closed_flat(self, x, y, n):
        """Create a closed flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*125
            p = (x+1, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+70)
            self.beams.append(Polygon(p, 85, 20, self.space))
            p = (x+30, y-30)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def horizontal_pile(self, x, y, n):
        """Create a horizontal pile"""
        y += 70
        for i in range(n):
            p = (x, y+i*20)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def vertical_pile(self, x, y, n):
        """Create a vertical pile"""
        y += 10
        for i in range(n):
            p = (x, y+85+i*85)
            self.columns.append(Polygon(p, 20, 85, self.space))

    def load_level(self):
        if self.number == 0:
            self.pigs.append(Pig(980, 100, self.space))
            self.pigs.append(Pig(985, 182, self.space))

            for p in [(950, 80), (1010, 80), (950, 200), (1010, 200)]:
                # b = Rectangle(p, 'images/beam.png', self.space)

                self.columns.append(Polygon(p, 20, 85, self.space))
            
            for p in [(980, 240), (980, 150)]:
                self.beams.append(Polygon(p, 85, 20, self.space))
            
            self.number_of_birds = 8 if self.bool_space else 4

        elif self.number == 1:
            self.pigs.append(Pig(1000, 100, self.space))
            for p in [(900, 80), (850, 80), (850, 150), (1050, 150)]:
                self.columns.append(Polygon(p, 20, 85, self.space))

            p = (1105, 210)
            self.beams.append(Polygon(p, 85, 20, self.space))


        elif self.number == 2:
            self.pigs.append(Pig(880, 180, self.space))
            self.pigs.append(Pig(1000, 230, self.space))

            for p in [(880, 80), (1000, 80), (1000, 180)]:
                self.columns.append(Polygon(p, 20, 85, self.space))

            p = (1000, 210)
            self.beams.append(Polygon(p, 85, 20, self.space))
            p = (880, 150)
            self.beams.append(Polygon(p, 85, 20, self.space))

        elif self.number == 3:
            self.pigs.append(Pig(950, 320, self.space, 25))
            self.pigs.append(Pig(885, 225, self.space, 25))
            self.pigs.append(Pig(1005, 225, self.space, 25))

            for p in [(1100, 100), (1040, 100), (980, 100), (920, 100), (860, 100), 
                (800, 100), (860, 223), (920, 223), (980, 223), (1040, 223), (920, 350), (980, 350)]:
                self.columns.append(Polygon(p, 20, 85, self.space))
           
            for p in [(890, 280), (1010, 280), (950, 300), (950, 400), (1070, 152), 
                (950, 152), (1010, 180), (830, 152), (890, 180)]:
                self.beams.append(Polygon(p, 85, 20, self.space))

        elif self.number == 4:
            self.pigs.append(Pig(900, 300, self.space))
            self.pigs.append(Pig(1000, 500, self.space))
            self.pigs.append(Pig(1100, 400, self.space))

        elif self.number == 5:
            self.pigs.append(Pig(900, 70, self.space))
            self.pigs.append(Pig(1000, 152, self.space))
            
            for i in range(9):
                p = (800, 70+i*21)
                self.beams.append(Polygon(p, 85, 20, self.space))
            for i in range(4):
                p = (1000, 70+i*21)
                self.beams.append(Polygon(p, 85, 20, self.space))
            p = (970, 176)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (1026, 176)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (1000, 230)
            self.beams.append(Polygon(p, 85, 20, self.space))

        elif self.number == 6:
            self.pigs.append(Pig(920, 533, self.space, 40))
            self.pigs.append(Pig(820, 533, self.space))
            self.pigs.append(Pig(720, 633, self.space))
            
            self.closed_flat(895, 423, 1)
            self.vertical_pile(900, 0, 5)
            self.vertical_pile(926, 0, 5)
            self.vertical_pile(950, 0, 5)

        elif self.number == 7:
            self.pigs.append(Pig(978, 180, self.space, 30))
            self.pigs.append(Pig(978, 280, self.space, 30))
            self.pigs.append(Pig(978, 80, self.space, 30))
            
            self.open_flat(950, 0, 3)
            self.vertical_pile(850, 0, 3)
            self.vertical_pile(830, 0, 3)

        elif self.number == 8:
            self.pigs.append(Pig(1000, 180, self.space, 30))
            self.pigs.append(Pig(1078, 280, self.space, 30))
            self.pigs.append(Pig(900, 80, self.space, 30))
            
            self.open_flat(1050, 0, 3)
            self.open_flat(963, 0, 2)
            self.open_flat(880, 0, 1)

        elif self.number == 9:
            self.pigs.append(Pig(1000, 180, self.space))
            self.pigs.append(Pig(900, 180, self.space))
            
            self.open_flat(1050, 0, 3)
            self.open_flat(963, 0, 2)
            self.open_flat(880, 0, 2)
            self.open_flat(790, 0, 3)

        elif self.number == 10:
            self.pigs.append(Pig(960, 250, self.space))
            self.pigs.append(Pig(820, 160, self.space))
            self.pigs.append(Pig(1100, 160, self.space))
            
            self.vertical_pile(900, 0, 3)
            self.vertical_pile(930, 0, 3)
            self.vertical_pile(1000, 0, 3)
            self.vertical_pile(1030, 0, 3)
            self.horizontal_pile(970, 250, 2)
            self.horizontal_pile(820, 0, 4)
            self.horizontal_pile(1100, 0, 4)

        elif self.number == 11:
            self.pigs.append(Pig(820, 177, self.space))
            self.pigs.append(Pig(960, 150, self.space))
            self.pigs.append(Pig(1100, 130, self.space))
            self.pigs.append(Pig(890, 270, self.space, 30))
            
            self.horizontal_pile(800, 0, 5)
            self.horizontal_pile(950, 0, 3)
            self.horizontal_pile(1100, 0, 2)
            self.vertical_pile(745, 0, 2)
            self.vertical_pile(855, 0, 2)
            self.vertical_pile(900, 0, 2)
            self.vertical_pile(1000, 0, 2)
            p = (875, 230)
            self.beams.append(Polygon(p, 85, 20, self.space))

        self.number_of_birds = 4 if not self.bool_space else 8