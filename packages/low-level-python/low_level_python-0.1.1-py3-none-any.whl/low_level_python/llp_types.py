import ctypes

types = {
        "void": None,
        "char": ctypes.c_char,
        "char*": ctypes.c_char_p,
        "const char*": ctypes.c_char_p,
        "wchar_t": ctypes.c_wchar,
        "wchar_t*": ctypes.c_wchar_p,
        "bool": ctypes.c_bool,
        "int": ctypes.c_int,
        "unsigned int": ctypes.c_uint,
        "long": ctypes.c_long,
        "unsigned long": ctypes.c_ulong,
        "long long": ctypes.c_longlong,
        "unsigned long long": ctypes.c_ulonglong,
        "float": ctypes.c_float,
        "double": ctypes.c_double,
        "size_t": ctypes.c_size_t,
        "int8_t": ctypes.c_int8,
        "uint8_t": ctypes.c_uint8,
        "int16_t": ctypes.c_int16,
        "uint16_t": ctypes.c_uint16,
        "int32_t": ctypes.c_int32,
        "uint32_t": ctypes.c_uint32,
        "int64_t": ctypes.c_int64,
        "uint64_t": ctypes.c_uint64,
        "void*": ctypes.c_void_p,
    }

def set_ctypes(clibrary, function_name, return_type):
    """
    Set the return type of a C function in ctypes.
    
    :param clibrary: The loaded C library
    :param function_name: The name of the C function
    :param return_type: The C return type as a string
    """
    
    if return_type in types:
        getattr(clibrary, function_name).restype = types[return_type]
    else:
        raise ValueError(f"Unsupported return type: {return_type}")
    
