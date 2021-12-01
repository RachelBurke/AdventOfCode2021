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
    for (int i = 1; i < 2000; i++)
    {
        if (i == 1)
        {
            cout << lines[i - 1] << " (N/A - no previous measurement)" << endl;
        }

        if (lines[i - 1] < lines[i])
        {
            cout << lines[i] << " (increased)" << endl;
            count++;
        }
        else
        {
            cout << lines[i] << " (decreased)" << endl;
        }
    }

    cout << count; //1711

    return 0;
}