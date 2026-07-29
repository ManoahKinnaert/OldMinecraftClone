"""the task of this file is to generate all the blocks of the game and generate the sky of the minecraft world"""

from ursina import *
import time


class Sky(Entity):
    def __init__(self, sky_color=color.blue):
        super().__init__(
            parent=scene,
            model='sphere',
            color=sky_color,
            scale=300,
            double_sided=True)

# class for generating bedrock block
class BedrockBlock(Button):
    def __init__(self, position=(0, 0, 0), Block_texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=Block_texture,
            color=color.white,
            highlight_color=color.gray,
            collider="mesh")

# class for generating Stone block
class StoneBlock(Button):
    def __init__(self, position=(0, 0, 0), Block_texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=Block_texture,
            color=color.white,
            highlight_color=color.gray,
            collider="mesh")

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                t = 1000000
                Wait(t)
                destroy(self)

# class for generating Dirt block
class DirtBlock(Button):
    def __init__(self, position=(0, 0, 0), Block_texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=Block_texture,
            color=color.white,
            highlight_color=color.gray,
            collider="mesh")

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                t = 0.2
                time.sleep(t)
                destroy(self)


# class for generating Dirt block
class GrassBlock(Button):
    def __init__(self, position=(0, 0, 0), Block_texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=Block_texture,
            color=color.white,
            highlight_color=color.gray,
            collider="mesh")

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                t = 0.2
                time.sleep(t)
                destroy(self)

class TreeWoodBlock(Button):
    def __init__(self, position=(0, 0, 0), Block_texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=Block_texture,
            color=color.white,
            highlight_color=color.gray,
            collider="mesh")

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                t = 5
                time.sleep(t)
                destroy(self)

class TreeVineBlock(Button):
    def __init__(self, position=(0, 0, 0), Block_texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=Block_texture,
            color=color.white,
            highlight_color=color.gray,
            collider="mesh")

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)

class WoodenPlanckBlock(Button):
    def __init__(self, position=(0, 0, 0), Block_texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=Block_texture,
            color=color.white,
            highlight_color=color.gray,
            collider="mesh")

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                t = 5
                time.sleep(t)
                destroy(self)

class StoneBrickBlock(Button):
    def __init__(self, position=(0, 0, 0), Block_texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=Block_texture,
            color=color.white,
            highlight_color=color.gray)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                t = 5
                time.sleep(t)
                destroy(self)





