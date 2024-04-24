#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T; 

    while (T--) {
        int N, K;
        cin >> N >> K; 
        
        vector<int> A(N);
        for (int i = 0; i < N; ++i) {
            cin >> A[i]; 
        }

        int initial_sum = 0;
        for (int i = 0; i < N; ++i) {
            initial_sum += A[i]; 
        }

        
        sort(A.begin(), A.end());

        int max_sum = initial_sum;
        int flips_used = 0;

        
        for (int i = 0; i < N && flips_used < K; ++i) {
            
            int flipped_value = 7 - A[i];
            
            int increase = flipped_value - A[i];

            
            if (increase > 0) {
                max_sum += increase;
                ++flips_used;
            }
        }

        cout << max_sum << endl; 
    }

    return 0;
}
