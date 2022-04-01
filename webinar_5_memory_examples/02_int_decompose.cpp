#include <cstdint>
#include <cstdio>

int main() {
  int variable = 4;

  int *address = &variable;
  uint8_t *byte_address = reinterpret_cast<uint8_t *>(address);

  printf("address: %d \n", byte_address);

  for (int i = 0; i < 4; i += 1) {
      printf("byte %d: %d \n", i, *(byte_address + i));
  }

  return 0;
}
