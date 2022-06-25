#include <iostream>
#include <vector>
// #include <queue>
#include <deque>
#include <unordered_map>
#include <string>
#include <sstream>

typedef unsigned long long ull;

template <class T>
const std::vector<T> GetSplitStringVec(const std::string& raw_data) {
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

  return v;
}

template <class T>
const std::deque<T> GetSplitStringDeq(const std::string& raw_data) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  std::deque<T> v;

  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    T data;
    std::istringstream iss(buf);
    iss >> data;
    v.push_back(data);
  }

  return v;
}

int main() {
  // Input ---
  std::string raw_nm_str;
  std::getline(std::cin, raw_nm_str);
  auto split_nm = GetSplitStringVec<ull>(raw_nm_str);
  //   std::cout << "n: " << split_nm[0] << std::endl;
  //   std::cout << "m: " << split_nm[1] << std::endl;
  ull n = split_nm[0];
  ull m = split_nm[1];

  std::vector<ull> k_list(m, 0);
  std::vector<std::deque<ull>> a_table(m, std::deque<ull>());
  // std::vector<std::vector<ull>> a_table(m);
  for (ull i = 0; i < m; i++) {
    std::string raw_a_list_str;
    ull k;
    std::getline(std::cin, raw_a_list_str);
    // std::cout << "raw_a_list_str: " << raw_a_list_str << std::endl;
    k_list[i] = std::stoull(raw_a_list_str);

    std::getline(std::cin, raw_a_list_str);
    auto split_data = GetSplitStringDeq<ull>(raw_a_list_str);
    a_table[i] = split_data;
  }

  // Confirm input-data.
  //   std::cout << std::endl;
  //   std::cout << "--- k_list ---" << std::endl;
  //   for (auto k : k_list) std::cout << k << std::endl;
  //   std::cout << std::endl;

  //   std::cout << "--- a_table ---" << std::endl;
  //   for (auto a_list : a_table) {
  //     for (auto a : a_list) std::cout << a << " ";
  //     std::cout << std::endl;
  //   }
  // --- Input

  ull found_num_color = n;
  while (found_num_color > 0) {
    std::unordered_map<ull, std::vector<ull>> color_cylinder_id_map;  // (color, c_id)

    bool found_pair = false;

    // 筒を一つ一つ評価
    for (ull i = 0; i < m; i++) {
      std::deque<ull>& a_list = a_table[i];
      if (a_list.size() >= 1) {
        const ull a_color = a_list[0];

        // map に登録。
        auto it = color_cylinder_id_map.find(a_color);
        if (it != color_cylinder_id_map.end()) {
          color_cylinder_id_map[a_color].push_back(i);
        } else {
          color_cylinder_id_map[a_color] = std::vector<ull>();
        //   color_cylinder_id_map[a_color].reserve(2 * 100000 + 10);
          color_cylinder_id_map[a_color].push_back(i);
        }

        // 同じ筒で連続で同じ色が出てくるか調べる。
        if (a_list.size() >= 2) {
          const ull a_color_below = a_list[1];
          if (a_color == a_color_below) {
            // a_list.erase(a_list.begin(), a_list.begin() + 2);
            a_list.pop_front();
            a_list.pop_front();
            found_num_color--;
            found_pair = true;
            break;
          }
        }
      }
    }

    if (!found_pair) {
      // 見つかった色の中で同じ色が２つあるか調べる。
      for (auto c_c_id : color_cylinder_id_map) {
        const ull a_color = c_c_id.first;
        std::vector<ull>& c_id_list = c_c_id.second;

        if (c_id_list.size() == 2) {
          // 筒２つから先頭要素を消す。
          std::deque<ull>& a_list1 = a_table[c_id_list[0]];
          std::deque<ull>& a_list2 = a_table[c_id_list[1]];
          //   a_list1.erase(a_list1.begin());
          //   a_list2.erase(a_list2.begin());
          a_list1.pop_front();
          a_list2.pop_front();
          found_num_color--;
          found_pair = true;
        }
      }
      if (!found_pair) break;
    }
  }
  if (found_num_color > 0)
    std::cout << "No" << std::endl;
  else
    std::cout << "Yes" << std::endl;

  return 0;
}
