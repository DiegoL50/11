import pygame

class SpinachExplosion:
    def __init__(self, duration=5000):
        self.duration = duration
        self.active = False
        self.end_time = 0

    def activate(self):
        self.active = True
        self.end_time = pygame.time.get_ticks() + self.duration

    def update(self):
        if self.active and pygame.time.get_ticks() > self.end_time:
            self.active = False

class BroccoliShield:
    def __init__(self, duration=5000):
        self.duration = duration
        self.active = False
        self.end_time = 0

    def activate(self):
        self.active = True
        self.end_time = pygame.time.get_ticks() + self.duration

    def update(self):
        if self.active and pygame.time.get_ticks() > self.end_time:
            self.active = False
