#include <iostream>

int main() {
    int T;
    std::cin >> T;

    while (T--) {
        int N;
        std::cin >> N;

        // Calculate the maximum number of cows possible
        int maxCows = N / 4;

        // Calculate the maximum number of chickens possible
        int maxChickens = (N - (maxCows * 4)) / 2;

        // Calculate the total number of animals
        int totalAnimals = maxCows + maxChickens;

        std::cout << totalAnimals << std::endl;
    }

    return 0;
}
