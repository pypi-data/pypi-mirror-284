from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wame.scene import Scene

from wame.vector import IntVector2, IntVector3

import pygame

class Text:
    '''UI Text'''

    def __init__(self, scene:'Scene', text:str, font:pygame.font.Font, color:IntVector3 | tuple[int, int, int]) -> None:
        '''
        Initialize a new text instance
        
        Parameters
        ----------
        scene : `wame.Scene`
            The scene to hook this instance to
        text : `str`
            The characters to be rendered
        font : `wame.Font`
            The font that is rendered
        color : `wame.IntVector3 | tuple[int, int, int]`
            The color of the text
        '''
        
        self._scene:'Scene' = scene

        self._font:pygame.font.Font = font
        self._color:IntVector3 = color if isinstance(color, IntVector3) else IntVector3.from_tuple(color)
    
        self._textRender:pygame.Surface = self._font.render(text, self._scene.engine.settings.antialiasing, self._color.convert())

        self._position:IntVector2 = None
    
    def render(self) -> None:
        '''
        Render the text to the screen
        
        Raises
        ------
        `ValueError`
            If the position was not set before rendering
        '''
        
        if self._position is None:
            error:str = "Position must be defined before the text can be rendered. Please use the Text.set_position() method"
            raise ValueError(error)

        self._scene.engine._screen.blit(self._textRender, self._position.convert())
    
    def set_position(self, position:IntVector2 | tuple[int, int]) -> None:
        '''
        Set the position of the text from the top left corner
        
        Parameters
        ----------
        position : `wame.IntVector2 | tuple[int, int]`
            The X, Y position values of the text
        '''
        
        self._position = position if isinstance(position, IntVector2) else IntVector2.from_tuple(position)
    
    def set_text(self, text:str) -> None:
        '''
        Set the text of the instance
        
        Parameters
        ----------
        text : `str`
            The characters to render
        '''
        
        self._textRender = self._font.render(text, self._scene.engine.settings.antialiasing, self._color.convert())