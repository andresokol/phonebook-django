import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


outer_var = []


def decorator(func):
    print("decorator starting!")

    var = outer_var
    print(ref_count(id(outer_var)))

    def wrapper():
        print("wrapper!")
        return func()

    print(ref_count(id(outer_var)))
    print("decorator returning!")
    return wrapper


print(ref_count(id(outer_var)))


@decorator
def function():
    print("function!")


print(ref_count(id(outer_var)))

function()
function()
function()
