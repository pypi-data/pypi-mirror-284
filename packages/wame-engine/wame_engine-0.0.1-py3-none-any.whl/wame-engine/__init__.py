'''
### Pygame Wrapper Designed to Make Games Easier to Create and Manage
Created with the people in mind by WilDev Studios
```python
# https://wildevstudios.net
```

### Basics
Wame exposes certain functions that allows the easy creation of game loops.
`Follow the format below to instantiate a basic engine`
```python
import wame

WINDOW_SIZE_X:int = 0
WINDOW_SIZE_Y:int = 0
WINDOW_SIZE:wame.IntVector2 = wame.IntVector2(WINDOW_SIZE_X, WINDOW_SIZE_Y)
# A window size of (0, 0) fills the screen (fullscreen)

engine:wame.Engine = wame.Engine(WINDOW_SIZE)

@engine.on_render() # Calls the function below every frame. There can be as many of these as you'd like.
def update() -> None:
    ... # Do something on the screen

@engine.on_key_pressed() # Calls the function when a key has been pressed down. Called once every press.
def key_down(key:str) -> None:
    ... # Do something

# Please consult documentation for more information about events

engine.start()
```
'''

from pygame.font import Font, SysFont

from wame.engine import Engine
from wame.vector import IntVector2, IntVector3
from wame.button import Button
from wame.scene import Scene
from wame.area import Area
from wame.text import Text