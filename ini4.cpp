#include <iostream>
using namespace std;

int main() {
    int a, b, sum = 0;

    cin >> a;
    cin >> b;

    for(a; a <= b; a++) {
        if(a % 2 != 0)
            sum += a;
    }

    cout << sum << endl;
    return 0;
}
