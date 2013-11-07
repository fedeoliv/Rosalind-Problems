// http://rosalind.info/problems/ini5/

#include <iostream>
#include <fstream>
using namespace std;

int main() {
    string line;
    ifstream file_ini5("rosalind_ini5.txt");
    ofstream output;
    short next = 0;

    output.open("output_ini5.txt");

    while(getline(file_ini5, line)) {
        if(next) {
            cout << line << endl;
            output << line << endl;
            next = 0;
        } else {
            next = 1;
        }
    }

    output.close();
    return 0;
}
