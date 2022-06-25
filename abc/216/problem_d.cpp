#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <set>

// typedef unsigned long long ull;
typedef unsigned long ul;

template <class T>
void GetSplitStringVec(const std::string& raw_data, std::vector<T>* v) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    T data;
    std::istringstream iss(buf);
    iss >> data;
    v->push_back(data);
  }
}

template <class T>
void GetSplitStringDeq(const std::string& raw_data, std::deque<T>* v) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    T data;
    std::istringstream iss(buf);
    iss >> data;
    v->push_back(data);
  }
}

template <class T>
void GetSplitStringQue(const std::string& raw_data, std::queue<T>* v) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    T data;
    std::istringstream iss(buf);
    iss >> data;
    v->push(data);
  }
}

int main() {
  // Input ---
  std::string raw_nm_str;
  std::getline(std::cin, raw_nm_str);
  std::vector<ul> split_nm;
  GetSplitStringVec<ul>(raw_nm_str, &split_nm);
  ul n = split_nm[0];
  ul m = split_nm[1];

  std::vector<ul> k_list(m, 0);
  std::vector<std::queue<ul>> a_table(m, std::queue<ul>());
  a_table.reserve(m + 1);
  std::vector<std::vector<ul>> color_ball_bucket(n + 10);
  std::set<ul> surface_color_set;

  for (ul i = 0; i < m; i++) {
    std::string raw_a_list_str;
    std::getline(std::cin, raw_a_list_str);
    k_list[i] = std::stoul(raw_a_list_str);

    std::getline(std::cin, raw_a_list_str);
    GetSplitStringQue<ul>(raw_a_list_str, &a_table[i]);

    // 表層の色の ID を登録。
    const ul surf_color = a_table[i].front();
    color_ball_bucket[surf_color].push_back(i);
    surface_color_set.insert(surf_color);
  }
  // --- Input

  // 表層のボールが２つある所を探す。
  std::queue<ul> todo;  // このキューから取り出した順にボールとっていく。
  for (auto surf_color : surface_color_set) {
    // 見つかったら登録。
    if (color_ball_bucket[surf_color].size() == 2) {
      const ul m_id1 = color_ball_bucket[surf_color][0];
      const ul m_id2 = color_ball_bucket[surf_color][1];

      todo.push(m_id1);
      todo.push(m_id2);
    }
  }

  while (!todo.empty()) {
    const ul m_id1 = todo.front();
    todo.pop();
    a_table[m_id1].pop();

    if (a_table[m_id1].size() == 0) continue;

    // 次の表層の色の ID を登録。
    const ul next_surf_color = a_table[m_id1].front();
    color_ball_bucket[next_surf_color].push_back(m_id1);

    // ２つ１組になっていたら todo に登録。
    if (color_ball_bucket[next_surf_color].size() == 2) {
      const ul m_id2 = color_ball_bucket[next_surf_color][0];

      todo.push(m_id1);
      todo.push(m_id2);
    }
  }

  bool a_table_has_data = false;
  for (auto a_list : a_table) {
    if (a_list.size() > 0) a_table_has_data = true;
  }

  if (a_table_has_data > 0)
    std::cout << "No" << std::endl;
  else
    std::cout << "Yes" << std::endl;

  return 0;
}
