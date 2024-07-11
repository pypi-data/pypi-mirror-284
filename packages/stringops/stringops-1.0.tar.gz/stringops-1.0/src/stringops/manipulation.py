from stringops.exceptions import InvalidManipulation, ManipulationError
from stringops.read import Read
# from stringops.manipulation import Manipulation

class Manipulation(str):
    """Class Manipulation: can be used to use many Manipulative operations on string

    ### Usage
    
    - import the Manipulation class

    >>> from stringops.manipulation import Manipulation

    - take any string

    >>> string = "one"
    
    - Create a Manipulation object which will basically act as an extended str class.
    
    >>> string = Manipulation(string)

    ### Prinitng

    printing will happen as usual like str

    >>> string = Manipulation("abc")
    >>> print(string)
    """
    
    def add(self, *values: str) -> super:
        """add: Add one or more string to the existing string"""
        string = str(self)
        for x in values:
            string += x
        
        return Manipulation(string) 
    
    def half(self, type: str):
        """
        cut the string into half and return left or right part

        Parameters:
            type(str): "left" or "right"
        
        >>> str_one = "abc"
        >>> str_one = Manipulation(str_one)
        >>> print(str_one)
        """
        mid = len(self) // 2
        if type == "left":
            return self[:mid+1]
        elif type == "right":
            return self[mid:]
        else:
            raise InvalidManipulation("unidentified type provided. Use either \"left\" or \"right\".")
    
    def __split(self, keyword: str) -> list[str]:
        string = str(self)
        return string.split(keyword)

    def split(self, sep: str = "", return_type: str | int = "all") -> list[str] | str:
        """split based on a keyword and return either all or a specific value

        Parameters:
            - keyword(str): keyword upon which the split will be carried out
            - return_type(str | int): return type specifies if all values after the split will be returned or just a specific value.
                Default: "all"
                Possible Values: "all" or index(int)
        
        Return:
            list[str] or str
        """
        if type(return_type) == str and return_type == "all":
            return self.__split(sep)
        elif type(return_type) == str and return_type != "all":
            raise InvalidManipulation("unidentified return_type paramenter.")
        elif type(return_type) == int:
            split = self.__split(sep)
            if return_type >= len(split) or return_type < 0:
                raise ManipulationError(ManipulationError.DEFAULT + f"{self}: index out of bounds.")
            else:
                return split[return_type]
        else:
            raise InvalidManipulation("Unknown Error")
    
    def convert_to_read(self) -> Read:
        return Read(self)