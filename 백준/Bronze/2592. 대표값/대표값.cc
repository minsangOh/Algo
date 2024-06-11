#include <iostream>
#include <vector>
#include <unordered_map>


using namespace std;

/* 최빈수 찾기 */
int modeNum(const vector<int> &lst) {
    unordered_map<int, int> frequency;
    for (int num: lst) {
        frequency[num]++;
    }
    int mode, maxValue = 0;
    for (const auto &pair: frequency) {
        if (pair.second > maxValue) {
            mode = pair.first;
            maxValue = pair.second;
        }
    }
    
    return mode;
}

/* 평균값 찾기 */
double avgNum(const vector<int> &lst) {
    if (lst.empty()) {
        return 0;
    }
    double sumNum = 0, len = 0;
    for (int num: lst) {
        sumNum += num;
        len++;
    }
    
    return sumNum / len;
}

int main() {
    vector<int> lst;
    int num;

    for (int i = 0; i < 10; ++i) {
        cin >> num;
        lst.push_back(num);
    }
    int mode = modeNum(lst);
    double avg = avgNum(lst);
    cout << avg << endl << mode << endl;

    return 0;
}

