/* http://rosalind.info/problems/sign/ */

#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    int n;
    int total = 1;
    ofstream output;

    cin >> n;
    vector<int> list_numbers(n);

    /* Inserting values into the array and calculating the total of permutations */
    for(int i = 0; i < n; i++) {
        list_numbers[i] = i + 1;
        total *= i + 1;
    }

    output.open ("output_sign.txt");
    total = total << n;

    output << total << endl;

    do {
        for (int i = 0; i < 1 << n; i++) {
            for (int j = 0; j < n; j++) {
                if (i & (1 << j))
                    output << "-";

                output << list_numbers[j] << " ";
            }

            output << endl;
        }
    } while (next_permutation(list_numbers.begin(), list_numbers.end()));

    output.close();
    return 0;
}
