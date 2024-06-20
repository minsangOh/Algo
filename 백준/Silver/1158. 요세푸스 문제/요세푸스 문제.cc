#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> lst;
    for (int i = 0; i < n; ++i) {
        lst.push_back(i + 1);
    }
    int startPoint = 0;

    cout << "<";
    while (!lst.empty()) {
        startPoint = (startPoint + k - 1) % lst.size();
        if (lst.size() > 1) {
            cout << lst[startPoint] << "," << " ";
        } else {
            cout << lst[startPoint] << ">";
        }
        lst.erase(lst.begin() + startPoint);

    }

    return 0;
}