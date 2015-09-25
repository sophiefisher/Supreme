#tile.py

import pyglet,collidable,util,viewport


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

#tilesheet_image=pyglet.resource.image('tiles.jpg')

#wood_image=tilesheet_image.texture.get_region(0,0,25,25)
#util.set_tile_anchor(wood_image)
#bamboo_image=tilesheet_image.texture.get_region(50,0,25,25)
#util.set_tile_anchor(bamboo_image)
#grass_image=tilesheet_image.texture.get_region(100,0,25,25)
#util.set_tile_anchor(grass_image)

crater_sheet=pyglet.resource.image('crater_tile.png')
crater_image=crater_sheet.texture.get_region(0,0,25,25)
util.set_tile_anchor(crater_image)

black_sheet=pyglet.resource.image('black.png')
black_image=black_sheet.texture.get_region(0,0,25,25)
util.set_tile_anchor(black_image)

tile_mapping={1:crater_image,
              2:black_image,
              3:grass_image}

solid_tile_types=[1,2,3]

class Tile(collidable.Collidable):
    

    def __init__(self, *args, **kwargs):

        super(Tile, self).__init__(*args, **kwargs)
        #self.is_tile=True
        

   

       
        
        
