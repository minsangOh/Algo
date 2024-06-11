#include <iostream>

using namespace std;

int main() {
    int station = 10;
    int maxPerson = 0;
    int nowPerson = 0;
    int inPerson, outPerson;
    for (int i = 0; i < station; ++i) {
        cin >> outPerson >> inPerson;
        nowPerson += (- outPerson + inPerson);
        if (maxPerson < nowPerson) {
            maxPerson = nowPerson;
        }
    }
    cout << maxPerson << endl;

    return 0;
}