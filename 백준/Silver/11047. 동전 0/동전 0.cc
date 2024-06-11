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

    // 내림차순 정렬
    sort(coins.rbegin(), coins.rend());

    int count = 0;
    for (int i = 0; i < n; ++i) {
        if (coins[i] <= k) {
            count += k / coins[i];
            k %= coins[i];
        }
    }

    cout << count << endl;

    return 0;
}
