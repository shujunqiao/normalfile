

#include <iostream>
#include <stdio.h>
#include <time.h>

using namespace std;
static int pu[9][9] = 
{
	0, 0, 0, 0, 1, 0, 0, 5, 4,
	8, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0,
	6, 5, 0, 4, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 2, 7, 3, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0,
	2, 1, 0, 0, 0, 0, 8, 0, 0,
	7, 0, 0, 0, 0, 0, 3, 0, 0,
	0, 0, 0, 3, 5, 0, 0, 0, 0
};

int isvalid(const int i, const int j)
{
	const int n = pu[i][j];
	const static int query[] = { 0, 0, 0, 3, 3, 3, 6, 6, 6 };
	int t, u; 

	for (t = 0; t < 9; t++)
		if (t != i && pu[t][j] == n || t != j && pu[i][t] == n)

			return 0;

	for (t = query[i]; t < query[i] + 3; t++)
		for (u = query[j]; u < query[j] + 3; u++)
			if ((t != i || u != j) && pu[t][u] == n)
				return 0;

	return 1;
}

void output(void)
{
	static int n;

	printf("Solution is:\n");

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++)
			cout << pu[i][j] << " ";
		cout << endl;
	}

	cout << endl;
}

void Try(const int n)
{
	if (n == 81)
	{
		output();
		return;
	}

	const int i = n / 9, j = n % 9;

	if (pu[i][j] != 0)
	{
		Try(n + 1);
		return;
	}

	for (int k = 0; k < 9; k++) {
		pu[i][j]++;
		if (isvalid(i, j))
			Try(n + 1);
	}

	pu[i][j] = 0;
}

int main(void)
{
	int i, j;
	//for (i = 0; i < 9; i++)
	//{
	//	for (j = 0; j < 9; j++)
	//	{
	//		cin >> pu[i][j];
	//	}
	//}

	time_t t1, t2;
	time(&t1);
	Try(0);

	time(&t2);
	printf("Today's date and time: %f", difftime(t2, t1));
	cin>>i;
	return 0;
}