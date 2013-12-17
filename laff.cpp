// http://rosalind.info/problems/laff/

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <fstream>

using namespace std;

vector<string> readFasta(char* filename) {
  string buf;
  string line;
  vector<string> records;
  fstream f(filename,ios::in);
  while(getline(f,line)) {

    if((line[0] == '>') && (buf.length() != 0)) {
      records.push_back(buf);
      buf.clear();
    } else if((line[0] == '>') && (buf.length() == 0)) {
	continue;
    } else {
      buf += line;
    }

  }
  records.push_back(buf);

  return records;
}

short BLOSUM62(char c1, char c2) {
    unsigned short i=0;
    unsigned short j=0;

    switch(c1) {
      case 'A' : i=0; break;
      case 'R' : i=1; break;
      case 'N' : i=2; break;
      case 'D' : i=3; break;
      case 'C' : i=4; break;
      case 'Q' : i=5; break;
      case 'E' : i=6; break;
      case 'G' : i=7; break;
      case 'H' : i=8; break;
      case 'I' : i=9; break;
      case 'L' : i=10; break;
      case 'K' : i=11; break;
      case 'M' : i=12; break;
      case 'F' : i=13; break;
      case 'P' : i=14; break;
      case 'S' : i=15; break;
      case 'T' : i=16; break;
      case 'W' : i=17; break;
      case 'Y' : i=18; break;
      case 'V' : i=19; break;
    }

    switch(c2) {
      case 'A' : j=0; break;
      case 'R' : j=1; break;
      case 'N' : j=2; break;
      case 'D' : j=3; break;
      case 'C' : j=4; break;
      case 'Q' : j=5; break;
      case 'E' : j=6; break;
      case 'G' : j=7; break;
      case 'H' : j=8; break;
      case 'I' : j=9; break;
      case 'L' : j=10; break;
      case 'K' : j=11; break;
      case 'M' : j=12; break;
      case 'F' : j=13; break;
      case 'P' : j=14; break;
      case 'S' : j=15; break;
      case 'T' : j=16; break;
      case 'W' : j=17; break;
      case 'Y' : j=18; break;
      case 'V' : j=19; break;
    }

    short blosum62[20][20] = { {4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0},
 		{-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3},
 		{-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3},
 		{-2, -2,  1,  6, -3, 0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3},
  		{0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1},
 		{-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2},
 		{-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2},
  		{0, -2, 0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3},
 		{-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3},
 		{-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3},
 		{-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1},
 		{-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2},
 		{-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1},
 		{-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1},
 		{-1, -2, -2, -1,-3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2},
  		{1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2},
  		{0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0},
 		{-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3},
 		{-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1},
  		{0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4}};


    return blosum62[i][j];
}

//Creates empty matrix with all zeros
int **zeros(int nrows, int ncols) {
    int **retval = new int*[nrows];
    for(unsigned int i=0; i < nrows; ++i) {
        retval[i] = new int[ncols];
        for(unsigned int j = 0; j < ncols; ++j) {
            retval[i][j] = 0;
	}
    }

    return retval;
}

int open_penalty = -11;
int extension_penalty = -1;

int match_score(char alpha, char beta) {
    if((alpha == '-') || (beta == '-'))
        return extension_penalty;

    return BLOSUM62(alpha, beta);
}

void water(string seq1, string seq2) {
    ofstream output;
    unsigned int m = seq1.length();
    unsigned int n = seq2.length(); // length of two sequences

    //Generate DP table and traceback path pointer matrix
    int **M = zeros(m+1, n+1); //the DP table
    int **Mx = zeros(m+1, n+1);
    int **My = zeros(m+1, n+1);

    int **pointer = zeros(m+1, n+1); //to store the traceback path

    int max_score = 0; //initial maximum score in DP table
    unsigned int max_i;
    unsigned int max_j;
    unsigned int i, j;

    //Calculate DP table and mark pointers
    for(i = 1; i < m + 1; i++) {
        for(j = 1; j < n + 1; j++) {
            int score_diagonal = M[i-1][j-1] + match_score(seq1[i-1], seq2[j-1]);
            int score_up = My[i-1][j-1] + match_score(seq1[i-1], seq2[j-1]);
            int score_left = Mx[i-1][j-1] + match_score(seq1[i-1], seq2[j-1]);

            M[i][j] = max(0,max(score_left, max(score_up, score_diagonal)));

            Mx[i][j] = max(M[i-1][j] + open_penalty,Mx[i-1][j] + extension_penalty);

            My[i][j] = max(M[i][j-1]+open_penalty,My[i][j-1]+extension_penalty);

            if(M[i][j] >= max_score) {
              max_i = i;
              max_j = j;
                  max_score = M[i][j];
            }

            if(M[i][j] == 0) {
                pointer[i][j] = 0; //0 means end of the path
                continue;
            }

            if(M[i][j] == score_diagonal) {
                pointer[i][j] = 3; // 3 means trace diagonal
                continue;
            }

            if(M[i][j] == score_up) {
                    pointer[i][j] = 2; //2 means trace left
                    continue;
            }
            if(M[i][j] == score_left) {
                    pointer[i][j] = 1; //1 means trace up
                    continue;
            }
        }
    }

    output.open("rosalind_laff_output.txt");

    cout << max_score << endl;
    output << max_score << endl;

    string align1, align2;

    i = max_i;
    j = max_j; //indices of path starting point

    //traceback, follow pointers
    while(1) {
        if(pointer[i][j] == 3) {
            align1 =  seq1[i-1] + align1;
            align2 = seq2[j-1] + align2;
            i -= 1;
            j -= 1;
        }
            else if(pointer[i][j] == 2) {
                align1 = align1;
            align2 = seq2[j-1] + align2;
                j -= 1;
        }
            else if(pointer[i][j] == 1) {
                align1 = seq1[i-1] + align1;
                align2 = align2;
            i -= 1;
        }

        if(pointer[i][j] == 0) break;
    }

    cout << align1 << '\n' << align2 << endl;
    output << align1 << '\n' << align2 << endl;

    output.close();
}

int main() {
  vector<string> records = readFasta("rosalind_laff.txt");
  water(records[0], records[1]);

  return 0;
}
