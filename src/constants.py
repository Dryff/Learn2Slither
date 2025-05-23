from enum import Enum

AGENT_STATE_SIZE = 24  
AGENT_ACTION_SIZE = 4

BOARD_WIDTH = 10
BOARD_HEIGHT = 10

INITIAL_SNAKE_LENGTH = 3

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

NUM_GREEN_APPLES = 2
NUM_RED_APPLES = 1

class CellType(Enum):
    EMPTY = 0
    WALL = 1
    SNAKE_HEAD = 2
    SNAKE_BODY = 3
    GREEN_APPLE = 4
    RED_APPLE = 5


VISION_CHAR_MAP = {
    CellType.EMPTY: '0',
    CellType.WALL: 'W',
    CellType.SNAKE_HEAD: 'H',
    CellType.SNAKE_BODY: 'S',
    CellType.GREEN_APPLE: 'G',
    CellType.RED_APPLE: 'R'
}

COLOR_BLACK = (0, 0, 0)
COLOR_HEAD = (0, 0, 150)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255) # For snake
