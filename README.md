# Example Python Project

## Setup
Before get started make sure that you have python > 3.6 installed (prefereably python3.11).
As well as venv in the corresponding python version.

Setup the package as follows:
``` shell
python3.11 -m venv .venv
```

Enter the environment with:
``` shell
source .venv/bin/activate
```

## Outline

### General Setup
 - Setup .venv
 - Install and use the repository.
 - What happens to 'git' if we install this ?
 - Inspect code
 - Create a new folder: shapes
 - new __init__.py file,  


### Create Shapes and Update Them
 - New base-class Shape(ABC): when is it good to create a base-class, (abstract_methods) 

 - create Rectangle (use property / setter). Use cases: check before assigning, easy computation, read-only property (surface)
	- axes_length [property / setter]
	- surface [property]

 - create Ellipse, create_circle (Class / factory_pattern)
	- @classmethod :  
	- @staticmethod: create_unit_circle_points(number, radius)

  Operator overloading: do not do it in python, just create two separate functions with hint what it does

 - Add colors both to the Shape & to the point -> do plotting of the points

 Takeaways:
 - Multiple inheritance: careful! Try to keep shallow structure. Best to only have 1 (abstract) base class. (Do we have an example?)
 - Keep classes small and light! That's easier to reuse (!)


### Dunder methods dos / don't
 - Compare two cuboids -> should they be the same (?)

 - Add two cuboids? What should it do? Should we do this?
 - Add to poses -> what should happen? -> What happens if we directly add it to one of them. How can this be avoided?!
  __add__ / __eq__ / __str__
 - What other dunder methods exist -> analyse a simple one with 
 - __new__


 Takeaways:
  - Make sure that the use case is meaningful and VERY intuitive! Do not try to come up with new fancy math / concepts(!)


### Delete class / del / Control-C Handler / Shutdown execution
 - __del__ 
 - __delete__
	
 Alternatives:
 - Control-C handler
 - On shutdown: @atexit.register

###  


## Further Links
- List of (common) decorators:
https://wiki.python.org/moin/Decorators






