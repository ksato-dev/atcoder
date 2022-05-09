#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::vector<unsigned long long> c_list(n);
    for (int i = 0; i < n; i++) {
        unsigned long long value;
        std::cin >> value;
        c_list[i] = value;
    }
    std::sort(c_list.begin(), c_list.end());;

    unsigned long long inf_val = (static_cast<unsigned long long>(1e9) + 7);
    unsigned long long ans = 1;
    for (int i = 0; i < n; i++) {
        // 順列の考え方で積算する。
        ans = ans * (c_list[i]-i);  // 一つ前より選択肢が一つ減る。
        ans = ans % inf_val;
        if (ans <= 0)
            break;
    }
    std::cout << ans << std::endl;
    return 0;
}
