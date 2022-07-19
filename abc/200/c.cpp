#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

#define Graph(T) std::vector<std::vector<T>>
typedef unsigned long long ull;
typedef unsigned long ul;
typedef long long ll;
typedef long l;

int main() {
    std::string raw_str;
    std::getline(std::cin, raw_str);

    std::vector<ull> a_mod_cnt_list(200, 0);
    std::getline(std::cin, raw_str);

    std::stringstream ss{raw_str};
    std::string buf;
    while (std::getline(ss, buf, ' ')) {
      ull data;
      std::istringstream iss(buf);
      iss >> data;
      a_mod_cnt_list[data % 200]++;
    }

    ull ans_cnt = 0;
    for (int a_mod = 0; a_mod < 200; a_mod++) {
        const ull cnt = a_mod_cnt_list[a_mod];

        // a_mod と同じ余りを作れる A の組み合わせ数は、以下で求まる。
        const ull ans = cnt * (cnt - 1) / 2;
        ans_cnt += ans;
    }

    std::cout << ans_cnt << std::endl;
    return 0;
}
