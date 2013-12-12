// http://rosalind.info/problems/asmq/

#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;
const int MAXN = 100000;

int ncontigs[MAXN], lengths[MAXN], total = 0, N50, N75, max_len = 0, minlen = INFINITY;

int main() {
    freopen("rosalind_asmq.txt", "r", stdin);

    string contig;

    while(cin >> contig) {
        ++ncontigs[contig.length()];
        total += contig.length();

        if (contig.length() > max_len)
            max_len = contig.length();

        if (contig.length() < minlen)
            minlen = contig.length();
    }

    N50 = ceil(0.5 * total);
    N75 = ceil(0.75 * total);

    for (int i = max_len; i >= minlen; --i)
        lengths[i] = lengths[i + 1] + i * ncontigs[i];

    reverse(lengths + minlen, lengths + max_len + 1);

    int ansN50 = max_len - (lower_bound(lengths + minlen, lengths + max_len + 1, N50) - (lengths + minlen));
    int ansN75 = max_len - (lower_bound(lengths + minlen, lengths + max_len + 1, N75) - (lengths + minlen));

    cout << ansN50 << ' ' << ansN75 << endl;

    return 0;
}
