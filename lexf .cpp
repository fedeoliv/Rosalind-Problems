// http://rosalind.info/problems/lexf/

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
    string next;
    ofstream output;
    int n = 2, j = 0;
    char symbol[] = "ANVJOKTUSW";

    output.open("output_lexi_order.txt");

    for(int i = 0; i < sizeof(symbol); i++) {
        for(int j = 0; j < sizeof(symbol); j++) {
            next = static_cast<string>(symbol).substr(j, n - 1);
            if(next != "" && symbol[i] != NULL)
                output << symbol[i] << next << endl;
        }
    }

    output.close();
    return 0;
}
