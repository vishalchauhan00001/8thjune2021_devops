Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import ctypes
>>> x=10
>>> id(x)
2278700313168
>>> ctypes.cast(2278700313168, ctypes.py_object).value
10
>>> 