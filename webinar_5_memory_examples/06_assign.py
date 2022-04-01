class MyList(list):
    def __init__(self):
        print("created")

    def __del__(self):
        print("destroyed")


def main():
    var = MyList()
    var2 = var
    var3 = var
    var4 = var


main()
