from memory_profiler import profile


@profile
def main():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)
    del b
    return a


if __name__ == "__main__":
    main()
