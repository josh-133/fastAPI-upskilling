from dataclasses import dataclass

from typing import List

@dataclass
class EType:
    etype: str

    def __post_init__(self):
        if not (len(self.etype) == 2 and self.etype.isalnum()):
            raise ValueError("error in etype")
        
@dataclass
class PType_short:
    ptype: str

    def __post_init__(self):
        if not (len(self.ptype) == 2 and self.ptype.isalnum()):
            raise ValueError("error in ptype")

@dataclass
class PType:
    ptype: str

    def __post_init__(self):
        if not (2 <= len(self.ptype) <= 3 and self.ptype.isalnum()):
            raise ValueError("error in ptype")

@dataclass
class CType:
    ctype: str

    def __post_init__(self):
        if not (len(self.ctype) == 2 and self.ctype.isalnum()):
            raise ValueError("error in ctype")
        
@dataclass
class array1:
    var1: CType
    var2: List[PType]
    

@dataclass
class array2:
    var1: str
    var2: List[CType]
    var3: List[str]


    