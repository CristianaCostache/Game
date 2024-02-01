level_map = [
 'x                        x',
 'x      P                 x',
 'x xx  xxx     xx         x',
 'x                        x',
 'x                        x',
 'x       xxx              x',
 'x       xxx              x',
 'x  xxxxx    xxxxxxxxxxxxxx',
 'x                        x',
 'x                        x',
 'x                        x']

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
speed = 8
left_limit = screen_width // 4
right_limit = screen_width - (screen_width // 4)
gravity = 0.8
jump_speed = -16