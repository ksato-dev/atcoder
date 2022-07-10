#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

typedef unsigned long long ull;
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

template <class T>
void dfs(const std::vector<std::vector<T>>& graph, const T& node_id,
         std::vector<bool>* visited) {
  if (visited->at(node_id)) return;
  visited->at(node_id) = true;

  for (const T adj_id : graph[node_id])
    if (!visited->at(adj_id)) dfs<T>(graph, adj_id, visited);
}
