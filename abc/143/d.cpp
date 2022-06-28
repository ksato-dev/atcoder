#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

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

int main() {
  std::string raw_string;
  int n;
  std::getline(std::cin, raw_string);
  n = std::stoi(raw_string);

  std::getline(std::cin, raw_string);
  std::vector<int> l_list;
  GetSplitStringVec<int>(raw_string, &l_list);
  std::sort(l_list.begin(), l_list.end());

  int ans = 0;
  for (int i = 0; i < n - 2; i++) {
    int a = l_list[i];
    for (int j = i + 1; j < n - 1; j++) {
      int b = l_list[j];
      for (int k = j + 1; k < n; k++) {
        int c = l_list[k];

        bool cond1 = (a < (b + c));
        bool cond2 = (b < (c + a));
        bool cond3 = (c < (a + b));
        if (cond1 && cond2 && cond3) ans++;
      }
    }
  }

  std::cout << ans << std::endl;
  return 0;
}
