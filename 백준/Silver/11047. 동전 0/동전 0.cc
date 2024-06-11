#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> coins(n);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    sort(coins.begin(), coins.end(), greater<int>());

    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (coins[i] <= k) {
            cnt += k / coins[i];
            k %= coins[i];
        }
    }

    cout << cnt << endl;

    return 0;
}
