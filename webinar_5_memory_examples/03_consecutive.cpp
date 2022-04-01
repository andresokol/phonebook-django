#include <cstdio>

int main() {
    int* array = new int[3];

    for (int i = 0; i < 3; i += 1) {
        *(array + i) = i;
        // array[i] = i;
    }

    for (int i = 0; i < 3; i += 1) {
        printf("%d\n", array[i]);
    }

    return 0;
}