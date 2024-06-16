#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    while (true) {
        string num;
        cin >> num;
        if (num == "0") break;

        string sortNum = num;
        reverse(sortNum.begin(), sortNum.end());

        if (num == sortNum) {
            cout << "yes" << endl;
        } else {
            cout << "no" << endl;
        }
    }

    return 0;
}
