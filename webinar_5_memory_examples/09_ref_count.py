import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


var = [3, 4, 5]
print(ref_count(id(var)))

var2 = var
print(ref_count(id(var)))

var3 = var
var4 = var
print(ref_count(id(var)))
