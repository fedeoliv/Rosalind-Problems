// http://rosalind.info/problems/lexv/

#include <cstdio>
#include <iostream>
using namespace std;

inline void getOrder(int, int);

char dataset[50];
char result[50];
int qtd = 0;

int main() {
    int n;
    char c;
    while ((c = getchar()) != '\n')
        if (c != ' ')
            dataset[qtd++] = c;

    cin >> n;

    getOrder(0, n);
    return 0;
}

inline void getOrder(int len, int n) {
    if (len != n) {
        for (int i = 0; i < qtd; i++) {
            result[len] = dataset[i];
            result[len + 1] = '\0';

            cout << result << endl;

            getOrder(len + 1, n);
            result[len] = '\0';
        }
    }
}
