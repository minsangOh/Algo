#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int>lst;
    int num;

    while (cin >> num) {
        lst.push_back(num);
    }

    sort(lst.begin(), lst.end());
    cout << lst[1];

    return 0;
}