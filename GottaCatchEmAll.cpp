#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T; 

    while (T--) {
        int N, X, Y;
        cin >> N >> X >> Y; 
        vector<int> difficulties(N);
        for (int i = 0; i < N; ++i) {
            cin >> difficulties[i]; 
        }

        int total_cost = 0;

        for (int i = 0; i < N; ++i) {
            int Ai = difficulties[i];
           
            int cost_normal = Ai * X;
            
            int cost_master = Y;
            
            total_cost += min(cost_normal, cost_master);
        }

        cout << total_cost << endl;
    }

    return 0;
}