#include <iostream>
/*
Costs: O(logn)
*/

int find_0(int A[], int p, int q){
    int m = (p+q)/2;
    if(A[m] == 0 && A[m+1] == 1)
        return m;
    if(A[m] == 1)
        return find_0(A, p, m-1);
    else
        return find_0(A, m+1, q);
    return -1;
}

int main(){
    int A[] = {0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1};
    int n = 12;
    int k = find_0(A,0,n-1);
    std::cout << "The position of 0 is: " << k << std::endl;
    return 0;
}