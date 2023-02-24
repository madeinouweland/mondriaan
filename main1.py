import arcade
import math
import random

SCREEN_WIDTH = 1080 / 4
SCREEN_HEIGHT = 1920 / 4
dimx = 18
dimy = 32
cellsize = SCREEN_WIDTH / dimx * .975
margin = cellsize * .5
colors = ["#ebebeb", "#ebebeb", "#ebebeb", "#f5d000" ,"#f90601", "#0074b4"]

class Rect:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.w = abs(x1 - x2)
        self.h = abs(y1 - y2)
        self.color = arcade.color_from_hex_string(color)

    def split(self):
        divi = random.randint(2, 3)
        if self.w > self.h:
            return Rect(self.x1, self.y1, self.x1 + self.w / divi, self.y2, random.choice(colors)), Rect(self.x1 + self.w / divi, self.y1, self.x2, self.y2, random.choice(colors))
        else:
            return Rect(self.x1, self.y1, self.x2, self.y1 + self.h / divi, random.choice(colors)), Rect(self.x1, self.y1 + self.h / divi, self.x2, self.y2, random.choice(colors))

class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "MONDRIAAN")
        arcade.set_background_color(arcade.color_from_hex_string("#000"))
        self.time = 0

    def make(self):
        self.rectangles = [Rect(0, 0, dimx, dimy, random.choice(colors))]
        for x in range(12):
            i = random.randint(0, len(self.rectangles) - 1)
            r1, r2 = self.rectangles[i].split()
            self.rectangles.pop(i)
            self.rectangles.append(r1)
            self.rectangles.append(r2)

    def setup(self):
        self.make()

    def on_draw(self):
        self.clear()
        for r in self.rectangles:
            arcade.draw_lrtb_rectangle_filled(r.x1 * cellsize + margin, r.x2 * cellsize, SCREEN_HEIGHT - r.y1 * cellsize - margin, SCREEN_HEIGHT - r.y2 * cellsize, r.color)

    def on_update(self, delta_time):
        self.time += delta_time
        if self.time > 2:
            self.make()
            self.time = 0

game = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
game.setup()
arcade.run()
