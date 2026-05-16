#include <iostream>

int binary_search(int A[], int p,int q, int x){
    int k = (p+q)/2;
    if(A[k] == x)
        return k;
    if(A[k] > x)
        return binary_search(A, p, k-1, x);
    else
        return binary_search(A, k+1, q, x);
    return -1;
}

int find_k(int A[], int p, int q){
    int m = (p+q)/2;
    if(A[m] > A[m+1])
        return m;
    if(A[m] >= A[1])
        return find_k(A, m+1, q);
    else
        return find_k(A, p, m-1);
    return 0;
}

int find_x(int A[], int x, int n){
    int max_pos = find_k(A,0,n-1);
    if(x == A[max_pos])
        return max_pos;
    if(x >= A[1]){
        return binary_search(A,1,max_pos-1,x);
    }
    else
        return binary_search(A,max_pos+1,n-1,x);
    return -1;
}   

int main(){
    int A[] = {9,13,16,18,19,23,28,31,37,42,0,1,2,5,7,8};
    int n = 16;
    int k = find_x(A,31, n);
    std::cout << "The k is: " << k << std::endl;
    return 0;
}
