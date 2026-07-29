from panda3d.core import loadPrcFileData

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import unlit_shader
from Blocks import *
import random


def main():
    app = Ursina()

    
    Entity.default_shader = unlit_shader
    #camera.shader = None

    window.fullscreen = True
    window.borderless = False


    bedrock_texture = load_texture('blocks/Bedrock.png')
    stone_texture = load_texture('blocks/Stone.png')
    dirt_texture = load_texture('blocks/Dirt.jpg')
    grass_texture = load_texture('blocks/Grassblock.png')

    Stone_layers = random.randint(20, 30)
    grass_layers = 1
    dirt_layers = random.randint(3, 5)

    for y in range(1):
        for z in range(10):
            for x in range(10):
                bedrock_block = BedrockBlock(position=(x, y, z), Block_texture=bedrock_texture)
                y_cord = y + 1
                for _ in range(Stone_layers):
                    stone_block = StoneBlock(position=(x, y_cord, z), Block_texture=stone_texture)
                    y_cord += 1
                for _ in range(dirt_layers):
                    dirt_block = DirtBlock(position=(x, y_cord, z), Block_texture=dirt_texture)
                    y_cord += 1
                for _ in range(grass_layers):
                    grass_block = GrassBlock(position=(x, y_cord, z), Block_texture=grass_texture)
                    y_cord += 1


    sky = Sky(sky_color=color.blue)
    player = FirstPersonController(x=0, y=37, z=0)

    app.run()

if __name__ == '__main__':
    main()
