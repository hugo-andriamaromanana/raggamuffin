from enum import Enum
from typing import List, Type, TypeVar

_T = TypeVar('_T', bound='Renum')


class Renum(Enum):
    """
    A reverse enum.
    
    This class creates an Enum that can be read.
    It inherits from Enum and has a get method.
    The auto() method uses the name of the variable as the value.
    
    Example:
    ```
    class BloodType(Renum):
        A = auto()
        B = auto()
        AB = auto()
        O = auto()
        
    >>> BloodType.A.value == "A"
    True
    >>> BloodType.read("A") == BloodType.A
    True
    
    ```
    """
    
    @classmethod
    def get(cls: Type[_T], value, soft=False) -> _T:
        """
        From the Enum value get the enum itself
                
        Args:
            value (Any): The value to invert.
            soft (bool, optional): If True, returns None if the value is not found. Defaults to False.
            
        Returns:
            Any: The enum member.
        """
        read = cls._value2member_map_.get(value)
        if read is None and not soft:
            raise ValueError(f"Value {value} not found in {cls.__name__}")
        return read
    
    @staticmethod
    def _generate_next_value_(
        name, start: int, count: int, last_values: List[str]
    ) -> str:
        """
        Generate the next value for the enum as the variable name or as a lowercase string
        depending on the auto_str setting.

        Args:
            name (str): The name of the enum.
            start (int): The start value.
            count (int): The count of the enum.
            last_values (List[str]): The last values of the enum.

        Returns:
            str: The generated value.
        """
        return name
