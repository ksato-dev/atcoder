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

struct UnionFind {
  //! ref:
  //! https://qiita.com/ofutonton/items/c17dfd33fc542c222396#union-find%E6%9C%A8%E3%81%AE%E5%8E%9F%E7%90%86%E3%81%A8%E3%82%BD%E3%83%BC%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89
  std::vector<int> par;  // par[i]:iの親の番号　(例) par[3] = 2 : 3の親が2

  UnionFind(int N) : par(N) {  //最初は全てが根であるとして初期化
    for (int i = 0; i < N; i++) par[i] = i;
  }

  int Root(int x) {  // データxが属する木の根を再帰で得る：Root(x) = {xの木の根}
    if (par[x] == x) return x;
    return par[x] = Root(par[x]);
  }

  void Unite(int x, int y) {  // xとyの木を併合
    int rx = Root(x);         // xの根をrx
    int ry = Root(y);         // yの根をry
    if (rx == ry) return;  // xとyの根が同じ(=同じ木にある)時はそのまま
    par[rx] =
        ry;  // xとyの根が同じでない(=同じ木にない)時：xの根rxをyの根ryにつける
  }

  bool Same(int x, int y) {  // 2つのデータx, yが属する木が同じならtrueを返す
    int rx = Root(x);
    int ry = Root(y);
    return rx == ry;
  }
};
