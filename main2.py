import arcade
import math
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 270, 480
CELLSIZE = SCREEN_WIDTH / 18 * .975
MARGIN = CELLSIZE * .5
COLORS = ["#ebebeb", "#ebebeb", "#ebebeb", "#f5d000" ,"#f90601", "#0074b4"]

class Rect:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.w = abs(x1 - x2)
        self.h = abs(y1 - y2)
        self.color = color

    def split(self):
        divi = random.randint(2, 3)
        if self.w > self.h:
            return Rect(self.x1, self.y1, self.x1 + self.w / divi, self.y2, self.color), Rect(self.x1 + self.w / divi, self.y1, self.x2, self.y2, random.choice(COLORS))
        else:
            return Rect(self.x1, self.y1, self.x2, self.y1 + self.h / divi, self.color), Rect(self.x1, self.y1 + self.h / divi, self.x2, self.y2, random.choice(COLORS))

class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "MONDRIAAN")
        arcade.set_background_color(arcade.color_from_hex_string("#000"))

    def setup(self):
        self.time = 0
        self.rectangles = [Rect(0, 0, 18, 32, random.choice(COLORS))]

    def on_draw(self):
        self.clear()
        for r in self.rectangles:
            arcade.draw_lrtb_rectangle_filled(r.x1 * CELLSIZE + MARGIN, r.x2 * CELLSIZE, SCREEN_HEIGHT - r.y1 * CELLSIZE - MARGIN, SCREEN_HEIGHT - r.y2 * CELLSIZE, arcade.color_from_hex_string(r.color))

    def on_update(self, delta_time):
        self.time += delta_time
        if self.time > .08:
            if len(self.rectangles) < 13:
                i = random.randint(0, len(self.rectangles) - 1)
                r1, r2 = self.rectangles[i].split()
                self.rectangles.pop(i)
                self.rectangles.append(r1)
                self.rectangles.append(r2)
                self.time = 0
            else:
                if self.time > 1.2:
                    self.time = 0
                    self.rectangles = [Rect(0, 0, 18, 32, random.choice(COLORS))]

game = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
game.setup()
arcade.run()
