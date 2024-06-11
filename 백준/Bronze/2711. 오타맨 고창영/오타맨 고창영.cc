#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        string word;
        int position;
        cin >> position >> word;

        word.erase(position - 1, 1);
        cout << word << endl;
    }

    return 0;
}