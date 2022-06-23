#include <iostream>
#include <vector>
#include <string>
#include <sstream>

typedef unsigned long long ull;

template<class T>
const std::vector<T> GetSplitStringList(const std::string &raw_data) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  std::vector<T> v;

  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    T data;
    std::istringstream iss(buf);
    iss >> data;
    v.push_back(data);
  }

  return v;  // v == {"", "a", "b", "", "c"}
}

int main() {
    std::string raw_nm_str;
    std::getline(std::cin, raw_nm_str);
    auto split_nm = GetSplitStringList<ull>(raw_nm_str);
    std::cout << "n: " << split_nm[0] << std::endl;
    std::cout << "m: " << split_nm[1] << std::endl;
    ull n = split_nm[0];
    ull m = split_nm[1];

    std::vector<ull> k_list(m, 0);
    std::vector<std::vector<ull>> a_table(m, std::vector<ull>());
    // std::vector<std::vector<ull>> a_table(m);
    for (ull i = 0; i < m; i++) {
        std::string raw_a_list_str;
        ull k;
        std::getline(std::cin, raw_a_list_str);
        // std::cout << "raw_a_list_str: " << raw_a_list_str << std::endl;
        k_list[i] = std::stoull(raw_a_list_str);

        std::getline(std::cin, raw_a_list_str);
        auto split_data = GetSplitStringList<ull>(raw_a_list_str);
        a_table[i] = split_data;
    }

    // Confirm input-data.
    std::cout << std::endl;
    std::cout << "--- k_list ---" << std::endl;
    for (auto k : k_list)
        std::cout << k << std::endl;
    std::cout << std::endl;

    std::cout << "--- a_table ---" << std::endl;
    for (auto a_list : a_table) {
      for (auto a : a_list) std::cout << a << " ";
      std::cout << std::endl;
    }

    return 0;
}