#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    const unsigned long long inf_val = (unsigned long long)(1e9) + 7;
    unsigned long long n;
    std::cin >> n;

    std::vector<unsigned long long> c_list(n);
    for (unsigned long long i = 0; i < n; i++)
        std::cin >> c_list[i];

    std::sort(c_list.begin(), c_list.end());

    bool is_a_list = true;
    unsigned long long count_a_list = 1;

    for (unsigned long long i = 0; i < n; i++)
    {
        const unsigned long long diff = c_list[i] - i;
        if (diff <= 0)
        {
            is_a_list = false;
            break;
        }
        else
            count_a_list = count_a_list % inf_val;
        count_a_list *= diff;
    }

    if (is_a_list)
        std::cout << count_a_list % inf_val << std::endl;
    else
        std::cout << 0 << std::endl;

    return 0;
}
