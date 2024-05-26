#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    long long length = 0;
    long long digits = 1;
    long long power10 = 10;

    while (n >= power10) {
        length += (power10 - (power10 / 10)) * digits;
        digits++;
        power10 *= 10;
    }

    length += (n - (power10 / 10) + 1) * digits;

    cout << length << "\n";

    return 0;
}
