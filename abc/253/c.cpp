#include <iostream>
#include <istream>
#include <sstream>
#include <set>
#include <string>
#include <vector>

typedef unsigned long long ull;

const std::vector<std::string> GetSplitStringList(const std::string &raw_data) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  std::vector<std::string> v;

  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    v.push_back(buf);
  }

  return v;  // v == {"", "a", "b", "", "c"}
}

int main() {
  std::string raw_data;
  std::getline(std::cin, raw_data);
  ull q = std::stoull(raw_data);
  std::multiset<ull> s;

  for (ull q_id = 0; q_id < q; q_id++) {
    // ref split string: https://marycore.jp/prog/cpp/std-string-split/
    std::string raw_data;
    std::getline(std::cin, raw_data);
    auto split_stirng_list = GetSplitStringList(raw_data);

    const int q_type = std::stoi(split_stirng_list[0]);

    ull x, c;
    // Commnet: スイッチ文だと内部で変数宣言ができないので if
    // で実装したほうが良かった。
    switch (q_type) {
      case 1:
        /* code */
        x = std::stoull(split_stirng_list[1]);
        // std::cout << "x:" << x << std::endl;
        s.insert(x);
        break;
      case 2:
        /* code */
        x = std::stoull(split_stirng_list[1]);
        c = std::stoull(split_stirng_list[2]);
        // const ull erasing_num = std::min(c, )
        while (true) {
          if (c <= 0) break;
          auto s_itr = s.find(x);
          if (s_itr == s.end()) break;
          s.erase(s_itr);
          c--;
        }
        // s.insert(x);
        break;
      case 3:
        /* code */
        std::cout << *s.rbegin() - *s.begin() << std::endl;
        break;

      default:
        break;
    }
  }
  return 0;
}
