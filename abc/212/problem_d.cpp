#include <iostream>
#include <vector>
#include <string>
#include <sstream>

typedef unsigned long long ull;

const std::vector<std::string> get_data()
{
    std::vector<std::string> v;
    std::string s;
    std::cin >> s;
    std::stringstream ss{s};
    std::string buf;
    while (std::getline(ss, buf, ' '))
    {
        v.push_back(buf);
    }
    return v;
}

int main()
{
    ull q_num;
    std::cin >> q_num;

    std::vector<std::vector<std::string>> data_list;
    for (int q_id = 0; q_id < q_num; q_id++)
    {
        // std::cout << q_id << " ";
        auto data = get_data();
        data_list.push_back(data);
        // for (auto elem : data)
        //     std::cout << elem;
        // std::cout << std::endl;
        // std::cout << std::endl;
    }

    for (auto data : data_list)
    {
        std::stringstream ss;
        for (auto elem : data)
            ss << elem;
        std::cout << ss.str() << std::endl;
    }
    // std::cout << cnt << std::endl;
}