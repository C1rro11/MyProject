#include <iostream>
#include <vector>
#define rules  "Rules: Can't put a larger disc on top of a smaller one"

void Hanoing(int n, std::vector<int>& pegA, std::vector<int>& pegB, std::vector<int>& pegC)
{
    if(n == 0) return;

    Hanoing(n-1, pegA, pegC, pegB);
    pegC.push_back(pegA.back()); // n =1 
    pegA.pop_back();
    Hanoing(n-1, pegB, pegA, pegC);

}

int main(){
    std::cout << rules << std::endl;
    std::vector<int> pegA, pegB, pegC;
    int biggest = 4; // the biggest disk
    int big = 3; // the largest disk
    int mid = 2; // the second smallest disk
    int small = 1; // the smallest disk
    pegA = {biggest,big,mid,small}; //大中細
    pegB = {};
    pegC = {};
    int n = 4;
    Hanoing(n, pegA, pegB, pegC);
    std::cout << "pegA: ";
    for(int i = 0; i < pegA.size(); i++){
        std::cout << pegA[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "pegB: ";
    for(int i = 0; i < pegB.size(); i++){
        std::cout << pegB[i] << " ";
    }
    std::cout << '\n' << "pegC: ";
    for(int i = 0; i < pegC.size(); i++){
        std::cout << pegC[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}