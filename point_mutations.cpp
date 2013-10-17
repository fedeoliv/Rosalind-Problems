#include <iostream>
#include <cstring>

using namespace std;

/* http://rosalind.info/problems/hamm/ */

int main() {
    int sum = 0;
    const char s[] = "GAGCCTACTAACGGGAT";
    const char t[] = "CATCGTAATGACGGCCT";

    for(int i = 0; i < strlen(s); i++) {
        if(s[i] != t[i]) {
            sum++;
        }
    }

    cout << sum << endl;
}
