#include <bits/stdc++.h>
using namespace std;

int maxMeetings(int start[], int end[], int n)
{
    vector<pair<int, int>> v;

    for (int i = 0; i < n; i++)
    {
        v.push_back(make_pair(end[i], start[i]));
    }
    sort(v.begin(), v.end()); // sorting based on end time as it is the first in the pair
    int pre_end = v[0].first; // ending time of first meeting
    int count = 1;
    for (int i = 1; i < n; i++)
    {
        if (pre_end < v[i].second)
        { // condition to check that the next meeting's starting time is after that of the ending time of previously included meeting
            count++;
            pre_end = v[i].first;
        }
    }
    return count;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    cin >> t;
    int n;
    int start[n], end[n];

    while (t--)
    {
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> start[i];
        for (int i = 0; i < n; i++)
            cin >> end[i];

        cout << maxMeetings(start, end, n) << endl;
    }
}