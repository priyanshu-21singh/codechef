#include <stdio.h>

void canCompleteAssignments(int T, int testCases[]) {
    for (int i = 0; i < T; i++) {
        int X = testCases[i];
        int totalTimeNeeded = 3; // 3 assignments
        int startTime = X;
        int completionTime = startTime + totalTimeNeeded;
        
        if (completionTime <= 10) {
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    
    int testCases[T];
    for (int i = 0; i < T; i++) {
        scanf("%d", &testCases[i]);
    }
    
    canCompleteAssignments(T, testCases);
    
    return 0;
}