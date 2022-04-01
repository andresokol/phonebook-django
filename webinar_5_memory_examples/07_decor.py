def decorator(func):
    print("decorator starting!")

    def wrapper():
        print("wrapper!")
        return func()

    print("decorator returning!")
    return wrapper


@decorator
def function():
    print("function!")


function()
function()
function()
