#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
#include <utility>
#include <functional>

typedef unsigned long long ull;

int main() {
    std::string s, t;
    std::getline(std::cin, s);
    std::getline(std::cin, t);
    ull n_s = s.size();
    ull n_t = t.size();
    
    if (n_s > n_t) {
        std::cout << "No" << std::endl;
        return 0;
    }

    // 連続した文字を潰して一致するかどうか見る。
    std::string compressed_s = "";
    compressed_s += s[0];
    std::vector<std::pair<char, ull>> compressed_s_cnt;
    auto data_s = std::make_pair(s[0], 1);
    compressed_s_cnt.push_back(data_s);

    for (ull i = 1; i < n_s; i++) {
        if (s[i] == s[i - 1]) {
            ull size_array = compressed_s_cnt.size();
            compressed_s_cnt[size_array - 1].second += 1;
        }
        else {
            auto tmp_data = std::make_pair(s[i], 1);
            compressed_s_cnt.push_back(tmp_data);
            compressed_s += s[i];
        }
    }

    std::string compressed_t = "";
    compressed_t += t[0];
    std::vector<std::pair<char, ull>> compressed_t_cnt;
    auto data_t = std::make_pair(t[0], 1);
    compressed_t_cnt.push_back(data_t);

    for (ull i = 1; i < n_t; i++) {
        if (t[i] == t[i - 1]) {
            ull size_array = compressed_t_cnt.size();
            compressed_t_cnt[size_array - 1].second += 1;
        }
        else {
            auto tmp_data = std::make_pair(t[i], 1);
            compressed_t_cnt.push_back(tmp_data);
            compressed_t += t[i];
        }
    }

    // ---
    std::string ans = "No";

    if (compressed_s == compressed_t) {
        ans = "Yes";
        for (ull i = 0; i < compressed_s.size(); i++) {
            auto s_cnt = compressed_s_cnt[i];
            auto t_cnt = compressed_t_cnt[i];

            const bool cond1 = s_cnt.first == t_cnt.first;
            const bool cond2 = s_cnt.second == t_cnt.second;
            const bool cond3 = s_cnt.second >= 2;
            const bool cond4 = s_cnt.second < t_cnt.second;

            bool flag = false;
            if (cond1) {
                if (cond2 || (cond3 && cond4)) {
                    flag = true;
                }
            }
            if (!flag) {
                ans = "No";
                break;
            }
        }
    }
    std::cout << ans << std::endl;
    return 0;
}
