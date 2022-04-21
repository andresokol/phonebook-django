import timeit
import random


def generate_random_word(word_len: int) -> str:
    letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    selected_letters = [random.choice(letters) for _ in range(word_len)]
    return "".join(selected_letters)


def rotate_left(word: str) -> str:
    return word[1:] + word[0]


def find_min_rotation(word):
    rotated = [word]

    current_rotation = word
    for _ in range(len(word)):
        current_rotation = rotate_left(current_rotation)
        rotated.append(current_rotation)

    rotated.sort()
    answer = rotated[0]

    return answer


def main():
    word = generate_random_word(32)
    print("Word:")
    print(word)

    min_rotation = find_min_rotation(word)
    print("Min rotation:")
    print(min_rotation)


if __name__ == "__main__":
    main()

    # time_passed = timeit.timeit(main, number=1000)
    # print(time_passed / 1000 * 1000, "ms per iteration")
