#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    unordered_map<char, int> frequency;

    int n;
    cin >> n;
    string name;

    for (int i = 0; i < n; ++i) {
        cin >> name;
        char firstName;
        firstName = name[0];
        frequency[firstName]++;
    }

    string lst;

    for (const auto &pair: frequency) {
        if (pair.second >= 5) {
            lst.append(1, pair.first);
        }
    }
    sort(lst.begin(), lst.end());

    if (!lst.empty()) {
        cout << lst << endl;
    } else {
        cout << "PREDAJA" << endl;
    }

    return 0;
}