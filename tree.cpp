/* http://rosalind.info/problems/tree/ */

#include <iostream>
#include <fstream>
#include <boost/lexical_cast.hpp>
using namespace std;
using namespace boost;

int main() {
    int n, elements = 0;
    string line;
    ifstream file_tree("rosalind_tree.txt");

    // Getting the first value of the file and converting it to int
    getline(file_tree, line);
    n = lexical_cast<int>(line);

    // Getting the total number of couple of elements
    while(std::getline(file_tree, line))
        elements++;

    file_tree.close();

    // Total number of edges = ('n' nodes - 1) - total number of elements
    cout << n - 1 - elements << endl;

    return 0;
}
