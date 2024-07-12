from __future__ import annotations

class IntVector2:
    '''Vector with 2 Integer Values: X and Y'''

    def __init__(self, x:int, y:int) -> None:
        '''
        Instantiate a new Vector with integer X and Y values
        
        Parameters
        ----------
        x : `int`
            The X value
        y : `int`
            The Y value
        
        Raises
        ------
        `ValueError`
            If any provided arguments are not integers
        '''
        
        if not isinstance(x, int):
            error:str = f"Value of X ({x}) is not an integer"
            raise ValueError(error)
    
        if not isinstance(y, int):
            error:str = f"Value of Y ({y}) is not an integer"
            raise ValueError(error)

        self.x:int = x
        self.y:int = y
    
    def __repr__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"
    
    @classmethod
    def from_tuple(cls, xy:tuple[int, int]) -> IntVector2:
        '''
        Instantiate a new Vector from a tuple with integer X and Y values
        
        Parameters
        ----------
        xy : `tuple[int, int]`
            The tuple with the X and Y values
        
        Raises
        ------
        `ValueError`
            If the provided items in the tuple are not integers
        '''
        
        return cls(xy[0], xy[1])
    
    def convert(self) -> tuple[int, int]:
        '''
        Converts this instance of `IntVector2` into a `tuple`
        
        Returns
        -------
        vector : `tuple[int, int]`
            Converted x and y values
        '''

        return (self.x, self.y)

class IntVector3:
    '''Vector with 2 Integer Values: X, Y, and Z'''

    def __init__(self, x:int, y:int, z:int) -> None:
        '''
        Instantiate a new Vector with integer X, Y, and Z values
        
        Parameters
        ----------
        x : `int`
            The X value
        y : `int`
            The Y value
        z : `int`
            The Z value
        
        Raises
        ------
        `ValueError`
            If any provided arguments are not integers
        '''
        
        if not isinstance(x, int):
            error:str = f"Value of X ({x}) is not an integer"
            raise ValueError(error)
    
        if not isinstance(y, int):
            error:str = f"Value of Y ({y}) is not an integer"
            raise ValueError(error)
    
        if not isinstance(z, int):
            error:str = f"Value of Z ({z}) is not an integer"
            raise ValueError(error)

        self.x:int = x
        self.y:int = y
        self.z:int = z
    
    def __repr__(self) -> str:
        return f"X: {self.x}, Y: {self.y}, Z: {self.z}"
    
    @classmethod
    def from_tuple(cls, xyz:tuple[int, int, int]) -> IntVector3:
        '''
        Instantiate a new Vector from a tuple with integer X, Y, and Z values
        
        Parameters
        ----------
        xyz : `tuple[int, int, int]`
            The tuple with the X, Y, and Z values
        
        Raises
        ------
        `ValueError`
            If the provided items in the tuple are not integers
        '''
        
        return cls(xyz[0], xyz[1], xyz[2])
    
    def convert(self) -> tuple[int, int, int]:
        '''
        Converts this instance of `IntVector3` into a `tuple`
        
        Returns
        -------
        vector : `tuple[int, int, int]`
            Converted x, y, and z values
        '''

        return (self.x, self.y, self.z)