// http://rosalind.info/problems/ini2/

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b;
    long result;

    cin >> a;
    cin >> b;

    cout << static_cast<long>(pow(a, 2) + pow(b, 2)) << endl;
}
