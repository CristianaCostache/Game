level_map = [
 '                  ',
 '      P            ',
 ' xx  xxx     xx   ',
 '                  ',
 '                  ',
 '                  ',
 '                  ',
 '                  ',
 '                  ',
 '                  ',
 '                  ']

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
speed = 8
left_limit = screen_width // 4
right_limit = screen_width - (screen_width // 4)
