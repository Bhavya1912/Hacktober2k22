#include <bits/stdc++.h>
#define ll long long
using namespace std;

int majorityElement(vector<int> &v, int size)
{

    unordered_map<int, int> freq;

    for (int i = 0; i < size; i++)
        freq[v[i]]++;

    int max = 0, ele = 0;

    for (auto it : freq)
    {
        if (it.second > max)
        {
            max = it.second;
            ele = it.first;
        }
    }

    if (max > size / 2)
        return ele;
    else
        return -1;
}

int main()
{

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    vector<int> v = {4, 3, 4, 5, 4, 4, 0};

    int size = v.size();
    int ans = majorityElement(v, size);
    cout << ans;
    return 0;
}