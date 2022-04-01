#include <chrono>
#include <cstdio>
#include <thread>

int main() {
  const int iterations = 1024;

  for (int i = 0; i < iterations; i += 1) {
    int *new_array = new int[1024];
    new_array[0] = i;
  }

  printf("done with arrays");
  std::this_thread::sleep_for(std::chrono::seconds(60));

  return 0;
}
