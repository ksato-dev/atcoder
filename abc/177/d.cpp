#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>

typedef unsigned long long ull;
typedef unsigned long ul;

template <class T>
void GetSplitStringVec(const std::string &raw_data, std::vector<T> *v) {
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

template<class T>
struct UnionFind {
  //! ref:
  //! https://qiita.com/ofutonton/items/c17dfd33fc542c222396#union-find%E6%9C%A8%E3%81%AE%E5%8E%9F%E7%90%86%E3%81%A8%E3%82%BD%E3%83%BC%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89
  std::vector<T> par;  // par[i]:iの親の番号　(例) par[3] = 2 : 3の親が2

  UnionFind(T N) : par(N) {  //最初は全てが根であるとして初期化
    for (T i = 0; i < N; i++) par[i] = i;
  }

  T Root(T x) {  // データxが属する木の根を再帰で得る：Root(x) = {xの木の根}
    if (par[x] == x) return x;
    return par[x] = Root(par[x]);
  }

  void Unite(T x, T y) {  // xとyの木を併合
    T rx = Root(x);         // xの根をrx
    T ry = Root(y);         // yの根をry
    if (rx == ry) return;  // xとyの根が同じ(=同じ木にある)時はそのまま
    par[rx] =
        ry;  // xとyの根が同じでない(=同じ木にない)時：xの根rxをyの根ryにつける
  }

  bool Same(T x, T y) {  // 2つのデータx, yが属する木が同じならtrueを返す
    T rx = Root(x);
    T ry = Root(y);
    return rx == ry;
  }
};

int main() {
  std::string raw_str;
  std::vector<ull> nm;
  std::getline(std::cin, raw_str);
  GetSplitStringVec<ull>(raw_str, &nm);
  ull n = nm[0];
  ull m = nm[1];

  std::vector<ull> a_list(m), b_list(m);
  // std::vector<std::vector<ull>> graph(n);
  UnionFind<ull> uf(n);

  for (ull i = 0; i < m; i++) {
    std::vector<ull> ab;
    std::getline(std::cin, raw_str);
    GetSplitStringVec<ull>(raw_str, &ab);
    ull a = ab[0] - 1;
    ull b = ab[1] - 1;
    uf.Unite(a, b);
  }

  std::set<ull> s;
  std::map<ull, std::vector<ull>> group_dict;
  for (ull i = 0; i < n; i++) {
    ull root_id = uf.Root(i);
    s.insert(root_id);
    if (group_dict.count(root_id) == 0) group_dict[root_id] = std::vector<ull>();
    group_dict[root_id].push_back(i);
  }

  std::vector<ull> group_size_list;
  ull cnt_group = group_dict.size();
  for (auto group: group_dict) {
    ull group_root = group.first;
    std::vector<ull> id_list = group.second;
    group_size_list.push_back(id_list.size());
  }
  std::sort(group_size_list.begin(), group_size_list.end());

  std::cout << group_size_list[cnt_group - 1] << std::endl;

  return 0;
}
