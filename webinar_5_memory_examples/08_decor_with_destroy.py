class MyList(list):
    def __init__(self):
        print("CREATED")

    def __del__(self):
        print("DESTROYED")


def decorator(func):
    print("decorator starting!")

    var = MyList()

    def wrapper():
        print("wrapper!")
        return func()

    print("decorator returning!")
    return wrapper


@decorator
def function():
    pass


function()
function()
function()
