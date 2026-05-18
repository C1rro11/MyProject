#include <iostream>
/*
Costs: O(logk)
*/

int find_0(int A[], int p, int r){
    if (p > r) return -1;
    int m = (p+r)/2;
    if(A[m + 1] <= r && A[m] == 0 && A[m+1] == 1)
        return m;
    if(A[m] == 0)
        return find_0(A, m+1, r);
    else
        return find_0(A, p, m-1);
    return -1;
}


int main(){
    int A[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1};
    int B[] = {0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};
    int C[] = {0,0,0,0,0,0,1};
    int D[] = {0,1,1,1,1,1};
    int E[] = {0,0,1,1};
    int k = 0;
    int n = sizeof(B)/sizeof(B[0]);
    int i = 1;
    int hi =0;
    int steps = 0;
    while(i < n && B[i] == 0){
        i = i * 2;
        std::cout << "Steps " << ++steps << " : i = " << i << std::endl;
    }
    k = find_0(B, i/2, hi = (i < n) ? i : n -1);
    std::cout << "The position of 0 is: " << k << std::endl;
    return 0;
}