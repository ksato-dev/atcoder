#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

int main () {
    long long n;
    std::cin >> n;

    const long long max_value = 200010;
    std::vector<long long> table(max_value, 0);

    for (long long i = 0; i < n; i++) {
      long long l;
      long long r;
      std::cin >> l >> r;
      table[l] += 1;
      table[r] += -1;
    }

    long long section_cnt = 0;  // 複数人ログインしてる区間の数
    long long pre_sum_section = 0;
    long long sum_section = 0;
    std::vector<std::pair<long long, long long>> merged_section_list;  // (l, r) 
    for (long long i = 0; i < max_value; i++) {
      sum_section += table[i];

      // (0 -> plus value) になるときに結合区間ができる。
      if (sum_section > 0 && pre_sum_section == 0) {
        // std::cout << i << ", "<< sum_section << std::endl;
        section_cnt++;
        std::pair<long long, long long> merged_section(i, i);  // r はダミーで入れとく。
        merged_section_list.push_back(merged_section);
      }

      // (plus value -> 0) になるときに結合区間が消える。
      if (sum_section == 0 && pre_sum_section > 0)
        merged_section_list[section_cnt - 1].second = i;

      pre_sum_section = sum_section;
    }

  // l をソートする。（しなくても良い？）
  // std::sort(merged_section_list.begin(), merged_section_list.end());

  for (long long i = 0; i < section_cnt; i++) {
    std::cout << merged_section_list[i].first << " "
              << merged_section_list[i].second << std::endl;
  }

}
