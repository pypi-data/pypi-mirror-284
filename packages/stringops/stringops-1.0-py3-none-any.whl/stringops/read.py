
# from stringops.manipulation import Manipulation

class Read(str):
    """class Read: for read operations on str
    ### Usage
    - can be used explicitly by importing the Read class

        >>> from stringops.read import Read
        >>> a = Read("abc")
    
    - or can be used implicitly from the Manipulation Class

        >>> from stringops.manipulation import Manipulation
        >>> a = Manipulation("abc")
        >>> a = a.convert_to_read()
    """

    def there(self, key: str) -> bool:
        """check whether a target is present in the string"""
        if key in self:
            return True
        
        return False    