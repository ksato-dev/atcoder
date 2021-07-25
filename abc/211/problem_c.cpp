#include <iostream>
#include <string>
#include <vector>
#include <map>

std::vector<int> get_matched_ids(std::string string, char c)
{
    std::vector<int> ret_matched_ids;
    for (int c_id = 0; c_id < string.size(); c_id++)
    {
        char chr = string[c_id];
        if (chr == c)
            ret_matched_ids.push_back(c_id);
    }

    return ret_matched_ids;
}

int main()
{
    std::string string;
    std::cin >> string;

    std::string name = "chokudai";
    std::map<char, std::vector<int>> ids_dict;
    ids_dict['c'] = get_matched_ids(string, 'c');
    ids_dict['h'] = get_matched_ids(string, 'h');
    ids_dict['o'] = get_matched_ids(string, 'o');
    ids_dict['k'] = get_matched_ids(string, 'k');
    ids_dict['u'] = get_matched_ids(string, 'u');
    ids_dict['d'] = get_matched_ids(string, 'd');
    ids_dict['a'] = get_matched_ids(string, 'a');
    ids_dict['i'] = get_matched_ids(string, 'i');

    int cnt = 0;
    for (auto c_id : ids_dict['c'])
    {
        for (auto h_id : ids_dict['h'])
        {
            if (c_id >= h_id)
                continue;
            for (auto o_id : ids_dict['o'])
            {
                if (h_id >= o_id)
                    continue;
                for (auto k_id : ids_dict['k'])
                {
                    if (o_id >= k_id)
                        continue;
                    for (auto u_id : ids_dict['u'])
                    {
                        if (k_id >= u_id)
                            continue;
                        for (auto d_id : ids_dict['d'])
                        {
                            if (u_id >= d_id)
                                continue;
                            for (auto a_id : ids_dict['a'])
                            {
                                if (d_id >= a_id)
                                    continue;
                                for (auto i_id : ids_dict['i'])
                                {
                                    if (a_id >= i_id)
                                        continue;
                                    cnt = cnt + 1;
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    std::cout << (cnt % (int(1e9) + 7)) << std::endl;
    // std::cout << cnt << std::endl;
}