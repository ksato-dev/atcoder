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
void dfs(const std::vector<std::vector<T>> &graph, const T &node_id,
         std::vector<bool> *visited) {
            if (visited->at(node_id)) return;
            visited->at(node_id) = true;

            for (const T adj_id : graph[node_id])
              if (!visited->at(adj_id)) dfs<T>(graph, adj_id, visited);
         }

int main() {
    std::string raw_str;
    std::vector<ul> nm;
    std::getline(std::cin, raw_str);
    GetSplitStringVec<ul>(raw_str, &nm);
    ul n = nm[0];
    ul m = nm[1];

    std::vector<ul> a_list(m), b_list(m);
    std::vector<std::vector<ul>> di_graph(n);

    for (ul i = 0; i < m; i++) {
        std::vector<ul> ab;
        std::getline(std::cin, raw_str);
        GetSplitStringVec<ul>(raw_str, &ab);
        di_graph[ab[0] - 1].push_back(ab[1] - 1);
    }

    ul ans = 0;
    for (ul i = 0; i < n; i++) {
        std::vector<bool> visited(n, false);
        dfs<ul>(di_graph, i, &visited);
        size_t true_count = std::count(visited.begin(), visited.end(), true);
        ans += true_count;
    }
    std::cout << ans << std::endl;


    return 0;
}
