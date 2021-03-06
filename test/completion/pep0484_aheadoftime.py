""" Pep-0484 type hinting with ahead of time annotations """

# python >= 3.6

somelist = [1, 2, 3, "A", "A"]
element : int
for element in somelist[0:3]:
    #? int()
    element


otherlist = [1, "A"]
for e in otherlist:
    #? int() str()
    e


test_string: str = "Hello, world!"
#? str()
test_string


char: str
for char in test_string:
    #? str()
    char


import numpy
somearrays = [numpy.ones((10, 10)), numpy.eye(10), 2, 2.3]
array : numpy.ndarray
for array in somearrays[0:2]:
    #? numpy.ndarray()
    array
