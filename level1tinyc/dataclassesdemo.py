from dataclasses import dataclass
@dataclass
class sample:
    name:str
    l=[]
    no=2
s=sample('hi')
print(s.name,s.l,s.no)