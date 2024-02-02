level_map = [
 'xxxxxx      B      B      B        xxxxxx',
 'xxxxxx     xxx    xxx    xxx    B  xxxxxx',
 'xxxxxx                B   xxxxxxxxxxxxxxx',
 'xxxxxx          B    xxxx          xxxxxx',
 'xxxxxx         xxxx                xxxxxx',
 'xxxxxx B                           xxxxxx',
 'xxxxxxxxxxxxxx  B                  xxxxxx',
 'xxxxxx         xxxx      B         xxxxxx',
 'xxxxxx             B  xxxx         xxxxxx',
 'xxxxxx   P      xxxx               xxxxxx',
 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx']

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
speed = 8
left_limit = screen_width // 4
right_limit = screen_width - (screen_width // 4)
gravity = 0.8
jump_speed = -16
coin_size = 50
