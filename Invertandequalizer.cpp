#include <bits/stdc++.h>
using namespace std;

int minOperationsToEqualize(const string &S) {
    int count0 = 0, count1 = 0;
    int N = S.length();
    
    // Count segments of 0's and 1's
    for (int i = 0; i < N;) {
        char current = S[i];
        int start = i;
        
        // Move to the end of the current segment
        while (i < N && S[i] == current) {
            i++;
        }
        
        if (current == '0') {
            count0++;
        } else {
            count1++;
        }
    }
    
    // Minimum number of operations needed to make all characters equal
    return min(count0, count1);
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        string S;
        cin >> N >> S;
        cout << minOperationsToEqualize(S) << endl;
    }
    return 0;
}
