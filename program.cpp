#include <fstream>
#include <string>
#include <map>
using namespace std;

int main()
{
	map<string, int> result;
	fstream file;
	file.open("musicans.txt");
	if (!file.is_open())
		return 0;
	while (!file.eof())
	{
		int num;
		file >> num;
		while (file.peek() != '\n')
		{
			string s;
			file >> s;
			if (result.count(s) == 0)
				result[s] = 1;
			else
				result[s] += 1;
		}
		file.get();
	}
}