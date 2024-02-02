LEVEL_MAP = [
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

TILE_SIZE = 64
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = len(LEVEL_MAP) * TILE_SIZE
SPEED = 8
LEFT_LIMIT = SCREEN_WIDTH // 4
RIGHT_LIMIT = SCREEN_WIDTH - (SCREEN_WIDTH // 4)
GRAVITY = 0.8
JUMP_SPEED = -16
COIN_SIZE = 50
