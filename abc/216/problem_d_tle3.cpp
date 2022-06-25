#include <iostream>
#include <vector>
// #include <queue>
#include <deque>
#include <unordered_map>
#include <string>
#include <sstream>
// #include <memory>

// typedef unsigned long long ull;
typedef unsigned long ul;

template <class T>
void GetSplitStringVec(const std::string& raw_data, std::vector<T>* v) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  // std::vector<T> v;

  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    T data;
    std::istringstream iss(buf);
    iss >> data;
    v->push_back(data);
  }
  // return v;
}

template <class T>
void GetSplitStringDeq(const std::string& raw_data, std::deque<T>* v) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  // std::deque<T> v;

  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    T data;
    std::istringstream iss(buf);
    iss >> data;
    v->push_back(data);
  }
  // return v;
}

int main() {
  // Input ---
  std::string raw_nm_str;
  std::getline(std::cin, raw_nm_str);
  std::vector<ul> split_nm;
  GetSplitStringVec<ul>(raw_nm_str, &split_nm);
  //   std::cout << "n: " << split_nm[0] << std::endl;
  //   std::cout << "m: " << split_nm[1] << std::endl;
  ul n = split_nm[0];
  ul m = split_nm[1];

  std::vector<ul> k_list(m, 0);
  std::vector<std::deque<ul>> a_table(m, std::deque<ul>());
  a_table.reserve(m + 1);
  // std::vector<std::vector<ul>> a_table(m);
  for (ul i = 0; i < m; i++) {
    std::string raw_a_list_str;
    ul k;
    std::getline(std::cin, raw_a_list_str);
    // std::cout << "raw_a_list_str: " << raw_a_list_str << std::endl;
    k_list[i] = std::stoul(raw_a_list_str);

    std::getline(std::cin, raw_a_list_str);
    // std::deque<ul> split_data;
    // GetSplitStringDeq<ul>(raw_a_list_str, &a_table[i]);
    // a_table[i] = split_data;
    std::stringstream ss{raw_a_list_str};
    std::string buf;
    ul pre_data = 0;
    while (std::getline(ss, buf, ' ')) {
      ul data = 0;
      std::istringstream iss(buf);
      iss >> data;

      if (data != 0 && pre_data == data) {
        a_table[i].pop_front();
        n--;  // ボールの数を減らす。
      } else {
        a_table[i].push_back(data);
      }
      pre_data = data;
    }
  }
  // --- Input

  ul found_num_color = n;
  while (found_num_color > 0) {
    std::unordered_map<ul, std::vector<ul>> color_cylinder_id_map;  // (color, c_id)
    color_cylinder_id_map.reserve(m);  // (color, c_id)

    bool found_pair = false;

    // 筒を一つ一つ評価
    for (ul i = 0; i < m; i++) {
      std::deque<ul>& a_list = a_table[i];
      if (a_list.size() >= 1) {
        const ul a_color = a_list[0];

        // map に登録。
        auto it = color_cylinder_id_map.find(a_color);
        if (it != color_cylinder_id_map.end()) {
          color_cylinder_id_map[a_color].push_back(i);
        } else {
          color_cylinder_id_map[a_color] = std::vector<ul>();
          color_cylinder_id_map[a_color].push_back(i);
        }
      }
    }

    // 見つかった色の中で同じ色が２つあるか調べる。
    for (auto c_c_id : color_cylinder_id_map) {
      const ul a_color = c_c_id.first;
      std::vector<ul>& c_id_list = c_c_id.second;

      if (c_id_list.size() == 2) {
        // 筒２つから先頭要素を消す。
        std::deque<ul>& a_list1 = a_table[c_id_list[0]];
        std::deque<ul>& a_list2 = a_table[c_id_list[1]];
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
  if (found_num_color > 0)
    std::cout << "No" << std::endl;
  else
    std::cout << "Yes" << std::endl;

  return 0;
}
