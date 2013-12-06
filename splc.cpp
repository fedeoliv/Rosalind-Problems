/* http://rosalind.info/problems/splc/ */

#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;

int main() {
    // Setting the codon table
    map<string, char> ct;
    ct["TTT"] = 'F'; ct["TTC"] = 'F'; ct["TTA"] = 'L'; ct["TTG"] = 'L';
    ct["TCT"] = 'S'; ct["TCC"] = 'S'; ct["TCA"] = 'S'; ct["TCG"] = 'S';
    ct["TAT"] = 'Y'; ct["TAC"] = 'Y'; ct["TAA"] = 'Z'; ct["TAG"] = 'Z';
    ct["TGT"] = 'C'; ct["TGC"] = 'C'; ct["TGA"] = 'Z'; ct["TGG"] = 'W';
    ct["CTT"] = 'L'; ct["CTC"] = 'L'; ct["CTA"] = 'L'; ct["CTG"] = 'L';
    ct["CCT"] = 'P'; ct["CCC"] = 'P'; ct["CCA"] = 'P'; ct["CCG"] = 'P';
    ct["CAT"] = 'H'; ct["CAC"] = 'H'; ct["CAA"] = 'Q'; ct["CAG"] = 'Q';
    ct["CGT"] = 'R'; ct["CGC"] = 'R'; ct["CGA"] = 'R'; ct["CGG"] = 'R';
    ct["ATT"] = 'I'; ct["ATC"] = 'I'; ct["ATA"] = 'I'; ct["ATG"] = 'M';
    ct["ACT"] = 'T'; ct["ACC"] = 'T'; ct["ACA"] = 'T'; ct["ACG"] = 'T';
    ct["AAT"] = 'N'; ct["AAC"] = 'N'; ct["AAA"] = 'K'; ct["AAG"] = 'K';
    ct["AGT"] = 'S'; ct["AGC"] = 'S'; ct["AGA"] = 'R'; ct["AGG"] = 'R';
    ct["GTT"] = 'V'; ct["GTC"] = 'V'; ct["GTA"] = 'V'; ct["GTG"] = 'V';
    ct["GCT"] = 'A'; ct["GCC"] = 'A'; ct["GCA"] = 'A'; ct["GCG"] = 'A';
    ct["GAT"] = 'D'; ct["GAC"] = 'D'; ct["GAA"] = 'E'; ct["GAG"] = 'E';
    ct["GGT"] = 'G'; ct["GGC"] = 'G'; ct["GGA"] = 'G'; ct["GGG"] = 'G';

    ifstream collection("rosalind_splicing.txt");
    ofstream output;
    string line, dna, intron;
    char c;
    int i = -3;

    getline(collection, line);

    while (getline(collection, line) && line.at(0) != '>')
        dna.append(line);

    while (getline(collection, line)) {
        if (line.at(0) == '>') {
            dna.erase(dna.find(intron), intron.length());
            intron.clear();
        } else {
            intron.append(line);
        }
    }

    dna.erase(dna.find(intron), intron.length());

    output.open ("output_splicing.txt");

    while ((c = ct[dna.substr(i += 3, 3)]) != 'Z')
        output << c;

    output << endl;
    output.close();
    return 0;
}
