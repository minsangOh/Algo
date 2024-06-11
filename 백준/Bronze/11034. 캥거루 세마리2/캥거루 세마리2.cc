#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    while (cin >> a >> b >> c) {
        int case1 = (c - b) - 1;
        int case2 = (b - a) - 1;
        cout << max(case1, case2) << endl;
    }
    return 0;
}