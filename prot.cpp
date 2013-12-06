#include <iostream>
#include <cstring>
using namespace std;

/* http://rosalind.info/problems/prot/ */

string encode_protein(string);

int main() {
    string protein = "";
    const string rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA";

    for(int i = 0; i < rna.size(); i+= 3) {
        protein += string(encode_protein(rna.substr(i, 3)));
    }

    cout << protein;
}

inline string encode_protein(string rna) {
    if(rna == "UUU" || rna == "UUC") {
        return "F";
    } else if(rna == "UUA" || rna == "UUG" || rna == "CUU" || rna == "CUC"
              || rna == "CUU" || rna == "CUC" || rna == "CUA" || rna == "CUG") {
        return "L";
    } else if(rna == "UCU" || rna == "UCC" || rna == "UCA" || rna == "UCG") {
        return "S";
    } else if(rna == "UAU" || rna == "UAC") {
        return "Y";
    } else if(rna == "UGU" || rna == "UGC") {
        return "C";
    } else if(rna == "UGG") {
        return "W";
    } else if(rna == "CCU" || rna == "CCC" || rna == "CCA" || rna == "CCG") {
        return "P";
    } else if(rna == "CAU" || rna == "CAC") {
        return "H";
    } else if(rna == "CAA" || rna == "CAG") {
        return "Q";
    } else if(rna == "CGU" || rna == "CGC" || rna == "CGA" || rna == "CGG") {
        return "R";
    } else if(rna == "AUU" || rna == "AUC" || rna == "AUA") {
        return "I";
    } else if(rna == "AUG") {
        return "M";
    } else if(rna == "ACU" || rna == "ACC" || rna == "ACA" || rna == "ACG") {
        return "T";
    } else if(rna == "AAU" || rna == "AAC") {
        return "N";
    } else if(rna == "AAA" || rna == "AAG") {
        return "K";
    } else if(rna == "AGU" || rna == "AGC") {
        return "S";
    } else if(rna == "AGA" || rna == "AGG") {
        return "R";
    } else if(rna == "GUU" || rna == "GUC" || rna == "GUA" || rna == "GUG") {
        return "V";
    } else if(rna == "GCU" || rna == "GCC" || rna == "GCA" || rna == "GCG") {
        return "A";
    } else if(rna == "GAU" || rna == "GAC") {
        return "D";
    } else if(rna == "GAA" || rna == "GAG") {
        return "E";
    } else if(rna == "GGU" || rna == "GGC" || rna == "GGA" || rna == "GGG") {
        return "G";
    }

    return "";
}
