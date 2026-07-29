from ursina import *
from Blocks import *


"""Textures """
bedrock_texture = load_texture('Bedrock.png')
stone_texture = load_texture('Stone.png')
dirt_texture = load_texture('Dirt.jpg')
grass_texture = load_texture('Grassblock.png')


Stone_layers = random.randint(int(20), int(30))
grass_layers = random.randint(int(1), int(2))
dirt_layers = random.randint(int(3), int(5))
for y in range(1):
    for z in range(10):
        for x in range(10):
            bedrock_block = BedrockBlock(position=(x, y, z), Block_texture=bedrock_texture)
            y_cord = y + 1
            for a in range(Stone_layers):
                stone_block = StoneBlock(position=(x, y_cord, z), Block_texture=stone_texture)
                y_cord += 1
            for a in range(dirt_layers):
                dirt_block = DirtBlock(position=(x, y_cord, z), Block_texture=dirt_texture)
                y_cord += 1
            for a in range(grass_layers):
                grass_block = GrassBlock(position=(x, y_cord, z), Block_texture=grass_texture)
                y_cord += 1