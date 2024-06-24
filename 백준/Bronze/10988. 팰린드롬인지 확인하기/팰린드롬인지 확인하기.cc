#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string word;
    cin >> word;
    string reverseWord = word;
    reverse(reverseWord.begin(), reverseWord.end());

    if (word == reverseWord) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
    return 0;
}