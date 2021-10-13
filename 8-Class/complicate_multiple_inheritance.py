
# source https://data-flair.training/blogs/python-multiple-inheritance/
class A:
                id=1            
class B:
                id=2             
class C:
                id=3              
class M(A,C,B):
                pass

print(M.__mro__)


# Depth Frist Search