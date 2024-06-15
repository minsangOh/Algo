#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    int n;
    string word;
    cin >> n;
    cin >> word;
    unordered_set<char> bigSet, smallSet;
    string bigRainbow = "ROYGBIV";
    string smallRainbow = "roygbiv";

    for (int i = 0; word[i]; i++) {
        if (isupper(word[i]) && bigRainbow.find(word[i]) != string::npos) {
            bigSet.insert(word[i]);
        } else if (islower(word[i]) && smallRainbow.find(word[i]) != string::npos) {
            smallSet.insert(word[i]);
        }
    }

    if (bigSet.size() < 7 && smallSet.size() < 7) {
        cout << "NO!" << endl;
    } else if (bigSet.size() >= 7 && smallSet.size() >= 7) {
        cout << "YeS" << endl;
    } else if (bigSet.size() >= 7) {
        cout << "YES" << endl;
    } else {
        cout << "yes" << endl;
    }

    return 0;
}
