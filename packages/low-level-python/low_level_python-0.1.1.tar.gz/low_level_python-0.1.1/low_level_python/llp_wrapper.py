import os
import ctypes
import functools
from low_level_python.llp_compiler import compile
from low_level_python.llp_types import set_ctypes

def includec(c_file):
    """
    A decorator generator for including and using C libraries in Python functions.

    This function checks for the existence of a compiled object file for the provided
    C source file. 

    Args:
        c_file (str): The name of the C source file (without extension) to be compiled and included.

    Returns:
        function: A decorator that, when applied to a Python function, injects the compiled C library 
        into the function global, making it accessible within the function.
    """
    dll_path = '__llp_cdll__/'
    if not os.path.exists(f'{dll_path}{c_file}.o') or True:
        compile(c_file)
    clibrary=None
    if os.path.exists(f'{dll_path}{c_file}.o'):
        try :
            clibrary = ctypes.CDLL(f'{dll_path}{c_file}.o')
        except Exception as e :
            print(e)
            return "Compilation failed"
        
    def decorator_includec(func):
        @functools.wraps(func)
        def wrapper_includec(*args, **kwargs):
            func.__globals__[c_file] = clibrary
            # set_ctypes(clibrary,'sayHello','char*')
            return func(*args, **kwargs)
        return wrapper_includec
    return decorator_includec

