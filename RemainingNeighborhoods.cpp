#include <iostream>

int main() {
    
    int N;
    std::cin >> N;
const int totalNeighborhoods = 100;

    
    int remainingNeighborhoods = totalNeighborhoods - N;

    
    std::cout << remainingNeighborhoods << std::endl;

    return 0;
}
