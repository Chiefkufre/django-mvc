
import pint as ps
from fractions import Fraction

def number_str_to_float(amount_str:str) -> (any, bool):
    """
    Take in an amount string to return float (if possible).
    
    Valid string returns:
    Float
    Boolean -> True
    Invalid string Returns
    Original String
    Boolean -> False
    
    Examples:
    1 1/2 -> 1.5, True
    32 -> 32.0, True
    Abc -> Abc, False
    """
    success = False
    number_as_float = amount_str
    try:
        number_as_float = float(sum(Fraction(s) for s in f"{amount_str}".split()))
    except:
        pass
    if isinstance(number_as_float, float):
        success = True
    return number_as_float, success


# print(number_str_to_float('2 1/3'))




def convert_to_system(self, quantity_as_float, unit, system=None, *args, **kwargs):
    if system is not None:
        ureg = ps.UnitRegistry(system=system)
        measurement = quantity_as_float * ureg(unit)
        return measurement

    else:
        pass
