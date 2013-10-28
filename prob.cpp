// http://rosalind.info/problems/prob/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>
#include <math.h>
using namespace std;

int main() {
    int g_count = 0, c_count = 0, frequencies = 0, result_dna = 0;
    double r;
    vector<string> values, results;
    string line, dna_str;
    ifstream file_prob ("rosalind_prob.txt");

    while(std::getline(file_prob, line)) {
        if(dna_str.empty()) {
            dna_str = line;

            for(int i = 0; i < dna_str.size(); i++) {
                if(dna_str[i] == 'C')
                    c_count++;
                else if(dna_str[i] == 'G')
                    g_count++;
            }
        } else {
            boost::split(values, line, ::isspace);
        }
    }

    file_prob.close();

    frequencies = c_count + g_count;
    result_dna = dna_str.size() - frequencies;

    for(int i = 0; i < values.size(); i++) {
        r = log10(pow((boost::lexical_cast<double>(values[i]) / 2.0), frequencies) * pow((0.5 - boost::lexical_cast<double>(values[i]) / 2.0), result_dna));
        cout << r << endl;
    }
}
