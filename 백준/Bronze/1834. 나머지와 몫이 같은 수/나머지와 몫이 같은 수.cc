#include <iostream>

using namespace std;

int main() {
    long long n, Sum = 0;
    cin >> n;
    for (int i = 1; i < n; ++i) {
        Sum += (n + 1) * i;
    }
    cout << Sum << endl;

    return 0;
}
