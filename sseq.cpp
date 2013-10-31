/* http://rosalind.info/problems/sseq/ */

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    string line, dna_str;
    vector<string> collection;
    vector<int> indices;
    ifstream file_sseq("rosalind_sseq.txt");
    int offset = 0, s, t;

    while(std::getline(file_sseq, line)) {
        if(line.substr(0, 1) != ">")
            collection.push_back(line);
    }

    file_sseq.close();

    for(int i = 0; i < collection[1].size(); i++) {
        for(int j = 0; j < collection[0].size(); j++) {
            if(collection[0][j] == collection[1][i]) {
                s = j + 1;
                break;
            }
        }

        offset += s;
        indices.push_back(offset);
        collection[0] = collection[0].substr(s, collection[0].size());
    }

    for(int i = 0; i < indices.size(); i++)
        cout << indices[i] << " ";

}
