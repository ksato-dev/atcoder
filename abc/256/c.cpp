#include <iostream>
#include <vector>

int main () {
    long long h1, h2, h3;
    long long w1, w2, w3;
    std::cin >> h1 >> h2 >> h3 >> w1 >> w2 >> w3;
    // std::cout << h1 << h2 << h3 << w1 << w2 << w3;
    // exit(-1);

    long long cnt = 0;
    for (long long v11 = 1; v11 < 31; v11++) {
      for (long long v12 = 1; v12 < 31; v12++) {
        for (long long v21 = 1; v21 < 31; v21++) {
          for (long long v32 = 1; v32 < 31; v32++) {
            for (long long v23 = 1; v23 < 31; v23++) {
              long long v31 = w1 - v11 - v21;
              long long v13 = h1 - v11 - v12;
              long long v22 = h2 - v21 - v23;
              long long v33 = w3 - v13 - v23;

              if (v31 <= 0 || v13 <= 0 || v22 <= 0 || v33 <= 0)
                continue;

            //   std::cout << v11 << " " << v12 << " " << v13 << std::endl;
            //   std::cout << v21 << " " << v22 << " " << v23 << std::endl;
            //   std::cout << v31 << " " << v32 << " " << v33 << std::endl;
            //   std::cout << std::endl;
              bool total_judge = true;
              if (h1 != v11 + v12 + v13) total_judge = false;
              if (h2 != v21 + v22 + v23) total_judge = false;
              if (h3 != v31 + v32 + v33) total_judge = false;

              if (w1 != v11 + v21 + v31) total_judge = false;
              if (w2 != v12 + v22 + v32) total_judge = false;
              if (w3 != v13 + v23 + v33) total_judge = false;

              if (total_judge) cnt++;
            }
          }
        }
      }
    }

    std::cout << cnt << std::endl;

}
