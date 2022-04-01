#include <cstdio>

int main() {
  int variable = 4;

  int *address = &variable;

  printf("%d %d", address, *address);

  return 0;
}
