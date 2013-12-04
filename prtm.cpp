#include <iostream>
#include <cstring>
using namespace std;

float weight_protein(char);

int main() {
    double weight = 0.0;
    const char sequence[] = "KVKKWILQKRRILQARTWQIETCLAHADSLMPCTRYSPMMEGICGIVVDQMECVAPDHTPTDDRSNMVCNGMSWKSSYWDCYDCHRSLFNRRRADNKVFMQTSDHHHLPDPMFWLAGKRFTARGVFQEVWPPFYAILHKDPRGMDGYEPGHEARCPWFITMSLFIMDKESIHHVRLNCIFYIKFWHTGYQIIRHTRGYCRARHDCGWDTQVGTARMVIPWYCVIACIRNSMTLDMLHVREDDHSYQILCEDQRATHISGNEFPSPDHPVGHPCMASCLGGNRGAEARSIHGRNATDKDVWPHMHSIENVGIGHMGDTRILRNYQAMGEEHVWKSWGDYQYKKWMFGNPYNFWCTIQPMWCHWWIQKFLHPLEGDNSQVRAWEETYDWCRCNIFPGEHVEPDREVYWFLRKRYKMDMCAPHWGVEPGCWDEYWHAPLMLITAFHFVCKTCGTAYVELNIYLHKIPTSIVVKNCTLRIWHTHGANTFVFGMEWMVTVMIHHKWYQEKCNTCDCRGWNHIYPEQMIIDLNWTLVHFGNRRPMAFMEFVTSKDEYNVHCHHQQKMQADSLVCGWCVGTKDKAWYAAYPFFNTFPAMYYHVYTIGFLDDILHRNMIWGMIRMAVLDYMMDEELEWYWEMLWHSHKMSKAHMVKSDCGGKPVRQELRCRIHIGGNRYTCKENKDYSLHYTVDMPWSGYEAPGVCKQIRRHDPKVCDSYIAPWWVIWKRPAVPDYWHMRWNHGAMMANLTEWHEEKNQVTHPKQISTYLTMRDIKTLWVFTLYTRNVEMWQWYLCDRPTERRIQTIDWHHIMSHACAFFHKTAHPCPGAHSRKNPTGMSIKRAVNHEIRERFGSMLGTQQ";
    std::cout.precision(7);

    for(int i = 0; i < strlen(sequence); i++) {
        weight += weight_protein(sequence[i]);
    }

    std::cout << std::fixed;
    cout << weight << endl;
}

float weight_protein(char protein) {
    if(protein == 'A')
        return 71.03711;
    else if(protein == 'C')
        return 103.00919;
    else if(protein == 'D')
        return 115.02694;
    else if(protein == 'E')
        return 129.04259;
    else if(protein == 'F')
        return 147.06841;
    else if(protein == 'G')
        return 57.02146;
    else if(protein == 'H')
        return 137.05891;
    else if(protein == 'I')
        return 113.08406;
    else if(protein == 'K')
        return 128.09496;
    else if(protein == 'L')
        return 113.08406;
    else if(protein == 'M')
        return 131.04049;
    else if(protein == 'N')
        return 114.04293;
    else if(protein == 'P')
        return 97.05276;
    else if(protein == 'Q')
        return 128.05858;
    else if(protein == 'R')
        return 156.10111;
    else if(protein == 'S')
        return 87.03203;
    else if(protein == 'T')
        return 101.04768;
    else if(protein == 'V')
        return 99.06841;
    else if(protein == 'W')
        return 186.07931;
    else if(protein == 'Y')
        return 163.06333 ;

    return 0.00000;
}
