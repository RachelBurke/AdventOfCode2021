#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    string Filename = "Day1Input.txt";
    ifstream input(Filename);
    string line;
    int lines[2000] = {0};
    int lineNum = 0;
    while (getline(input, line))
    {
        lines[lineNum] = stoi(line);
        lineNum++;
    }

    int count = 0;
    int sums[2000] = {0};
    for (int i = 2; i < 2000; i++)
    {
        sums[i - 2] = lines[i - 2] + lines[i - 1] + lines[i];
        if (i == 2)
        {
            cout << sums[i - 2] << " (N/A - no previous sum)" << endl;
        }

        if (sums[i - 3] < sums[i - 2])
        {
            cout << sums[i - 2] << " (increased)" << endl;
            count++;
        }
        else
        {
            cout << sums[i - 2] << " (decreased)" << endl;
        }
    }

    cout << count; //1743

    return 0;
}