import types
from dataclasses import dataclass, field

try:
    from types import UnionType
except:
    UnionType = None

def cast(val, typ):
    
    # all this for b***y python 3.9
    if isinstance(typ, str):

        if '|' not in typ:
            
            if isinstance(val, eval(typ)):
                return val

            return eval(typ)(val)

        subtypes = [eval(s) if s != 'None' else type(None)
                        for s in typ.split(' | ')]
    
    else:

        if isinstance(val, typ):
            return val

        if not isinstance(typ, UnionType):
            return typ(val)

        subtypes = typ.__args__

    for subtype in subtypes:
        try:
            val = cast(val, subtype)
        except Exception as e:
            continue
        else:
            return val

    raise e

class StrictDataClass:
    """A dataclass deriving from this will forcibly cast initialisation
parameters or throw an error.  A bit like pydantic, but arbitrary types
should work. Later assignment hasn't been checked properly"""

    def __post_init__(self) -> None:

       for name, field in self.__dataclass_fields__.items():

            try: 
                value = getattr(self, name)
            except AttributeError:
                continue

            type_ = field.type

            if not isinstance(value, type_):
                try:
                    object.__setattr__(self, name, cast(value, _type)) 
                except Exception as e:
                    msg = "dataclass field {name} initialised with wrong type"
                    raise TypeError(msg)

    def __setattr__(self, name: str, value: object) -> None:

        fields = self.__dataclass_fields__
        
        if name in fields:

            type_ = fields[name].type
            try:
                value = cast(value, type_)
            except:
                msg = "dataclass field {name} assigned with wrong type"
                raise TypeError(msg)
                
            object.__setattr__(self, name, value)

        else:
            
            super().__setattr__(name, value)
