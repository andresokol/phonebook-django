class MyList(list):
    def __init__(self):
        print("created")

    def __del__(self):
        print("destroyed")


variable = MyList()
# print(variable)
# variable.append(3)
# print(variable)
