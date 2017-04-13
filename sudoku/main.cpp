//#include <stdio.h>
//#include <stdlib.h>
//#include <iostream>
//
//using namespace std;
//#include "iostream"  
//#include "algorithm"  
//using namespace std;
//
//void permutation(char* str, int length)
//{
//	sort(str, str + length);
//	do
//	{
//		for (int i = 0; i < length; i++)
//			cout << str[i];
//		cout << endl;
//	} while (next_permutation(str, str + length));
//}
//int main(void)
//{
//	char str[] = "abcde";
//	cout << str << "所有全排列的结果为：" << endl;
//	permutation(str, 5);
//	system("pause");
//
//	int a[9][9];
//	a[0][0];
//	return 0;
//}

//int main(int argc, char* argv)
//{
//	int b = 10;
//	int sum = 0;
//
//	std::string astr = "a";
//	char chs[16];
//	sprintf_s(chs, 16, "chs:%x\n", astr);
//	cout << "chs:" << b << endl;
//	cout << "chs:" << chs << endl;
//
//	for (int i = 0; i < b; i++)
//	{
//		sum += i;
//		cout << sum << endl;
//	}
//	
//
//	int a;
//	cin >> a;
//	return 0;
//}

///main.cpp///主函数//里面有测试题目//  
//题目要求，数值为字符型，需要填的位置用字符‘.’代替。///  

#include <iostream>  
#include <stdlib.h>  
//#include "sudoku.h"  

using namespace std;

void sudoku(char array[9][9]); //解数独游戏函数。
void Conversion_char_int(char a[9][9], int p[9][9]); //转换函数，讲字符型数组 转化成整形数组，'.'变为0。
bool Inspection(int sudo[9][9]); //检查该题目是否合法。int Blank_number(int sudo[9][9]); //计算所给数独中待填入的空白数

typedef struct node //代表每个待填空格属性，包括对应的位置，以及可以取得值。
{
	int col; int row; int value[10];
}Node; //带有typedef 字样的结构体，在申请结构体变量的时候， Node 可以代替 struct node。

void Initialization_col_row(int sudo[9][9], Node * node_sudo); //确定Node结构体重每一个元素的 col 和row 的值。
int Find_value(int sudo[9][9], Node * node_sudo); //找该空格可能的解，并试着求第一个解。
void Solving(int sudo[9][9], int num_of_empty, Node* node_sudo); //解数独问题
void Print_sudo(int sudo[9][9]); //输出求得的数独的解。
int Blank_number(int sudo[9][9]);

int main()
{
	char arr[9][9] = { '5', '3', '.', '.', '7', '.', '.', '.', '.',
		'6', '.', '.', '1', '9', '5', '.', '.', '.',
		'.', '9', '8', '.', '.', '.', '.', '6', '.',
		'8', '.', '.', '.', '6', '.', '.', '.', '3',
		'4', '.', '.', '8', '.', '3', '.', '.', '1',
		'7', '.', '.', '.', '2', '.', '.', '.', '6',
		'.', '6', '.', '.', '.', '.', '2', '8', '.',
		'.', '.', '.', '4', '1', '9', '.', '.', '5',
		'.', '.', '.', '.', '8', '.', '.', '7', '9' };

	char arr_1[9][9] = { '.','9','.','1','.','.','5','.','.',
		'.','.','.','.','7','9','8','.','1',
		'2','.','.','.','.','.','.','.','6',
		'.','3','.','.','.','.','.','.','.',
		'.','.','.','7','8','1','.','.','.',
		'.','.','4','.','.','.','.','2','.',
		'7','.','.','6','.','.','.','.','4',
		'6','.','1','5','3','.','.','.','.',
		'.','.','9','.','.','7','.','6','.' };

	char arr_2[9][9] = { '.','.','2','.','6','.','.','.','.',
		'.','.',    '6',    '.',    '.',    '7',    '.',    '.',    '9',
		'.',    '.',    '7',    '.',    '.',    '8',    '4',    '.',    '.',
		'9',    '.',    '.',    '.',    '3',    '.',    '.',    '.',    '1',
		'3',    '.',    '.',    '5',    '.',    '2',    '.',    '.',    '4',
		'6',    '.',    '.',    '.',    '1',    '.',    '.',    '.',    '3',
		'.',    '.',    '5',    '3',    '.',    '.',    '8',    '.',    '.',
		'8',    '.',    '.',    '6',    '.',    '.',    '5',    '.',    '.',
		'.',    '.',    '.',    '.',    '2',    '.',    '9',    '.',    '.' };

	char arr_3[9][9] = { '8','.','.','.','.','.','.','.','.',
		'.','.',    '3',    '6',    '.',    '.',    '.',    '.',    '.',
		'.',    '7',    '.',    '.',    '9',    '.',    '2',    '.',    '.',
		'.',    '5',    '.',    '.',    '.',    '7',    '.',    '.',    '.',
		'.',    '.',    '.',    '.',    '4',    '5',    '7',    '.',    '.',
		'.',    '.',    '.',    '1',    '.',    '.',    '.',    '3',    '.',
		'.',    '.',    '1',    '.',    '.',    '.',    '.',    '6',    '8',
		'.',    '.',    '8',    '5',    '.',    '.',    '.',    '1',    '.',
		'.',    '9',    '.',    '.',    '.',    '.',    '4',    '.',    '.' };

	char arr_4[9][9] = { '.','4','.','.','.','3','5','.','.',
		'.',	'2',    '.',    '9',    '.',    '.',    '4',    '.',    '.',
		'.',    '.',    '6',    '.',    '.',    '.',    '.',    '.',    '.',
		'4',    '.',    '.',    '.',    '.',    '9',    '.',    '.',    '1',
		'.',    '3',    '.',    '7',    '.',    '.',    '.',    '2',    '.',
		'9',    '.',    '.',    '.',    '.',    '.',    '.',    '.',    '8',
		'.',    '.',    '.',    '.',    '.',    '.',    '3',    '.',    '.',
		'.',    '.',    '9',    '.',    '.',    '4',    '.',    '8',    '.',
		'.',    '.',    '8',    '1',    '.',    '.',    '.',    '7',    '.' };

	char arr_5[9][9] = {
		'.',	'1',	'.',	'.',	'.',	'6',	'.',	'.',	'.',
		'.',	'.',    '.',    '.',    '1',    '.',    '.',    '7',    '.',
		'.',    '2',    '.',    '.',    '.',    '.',    '.',    '.',    '9',
		'.',    '.',    '4',    '.',    '.',    '2',    '.',    '.',    '.',
		'.',    '.',    '.',    '.',    '3',    '.',    '.',    '5',    '.',
		'6',    '.',    '.',    '.',    '.',    '.',    '.',    '.',    '.',
		'3',    '.',    '.',    '4',    '.',    '.',    '.',    '.',    '.',
		'.',    '.',    '.',    '.',    '5',    '.',    '.',    '.',    '.',
		'.',    '.',    '7',    '.',    '.',    '.',    '9',    '.',    '8' };
	

	cout << "数独题目为：" << endl;
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
		{
			cout << arr_4[i][j] << "  ";
			if (j % 8 == 0 && j != 0)
			{
				cout << endl;
			}
		}

	sudoku(arr_4);

	int a;
	cin>>a;

	return 0;
}


void sudoku(char array[9][9])
{
	int sudo[9][9] = { 0 };
	int number_of_empty = 0;                                                   //定义需要填入数的个数  
	Conversion_char_int(array, sudo);                                        //转换成数字型 数独题目  
	if (!Inspection(sudo))                                                 //检查题目是否合法。  
	{
		cout << "该数独题目不符合要求，请检查后重新输入。" << endl;
		system("pause");
		exit(1);
	}
	number_of_empty = Blank_number(sudo);                     //计算需要填入数的个数  

	Node * node_sudu = (Node *)malloc(sizeof(Node)*number_of_empty);               //给每一个空格申请一个Node 结构体。  
	if (node_sudu == NULL)
	{
		cout << "Node结构体内存分配失败！" << endl;
		system("pause");
		exit(1);
	}

	Initialization_col_row(sudo, node_sudu);                              //确定Node结构体重每一个元素的  col 和row 的值。  

	Solving(sudo, number_of_empty, node_sudu);

}


void Conversion_char_int(char a[9][9], int p[9][9])                  //转换函数，讲字符型数组  转化成整形数组，'.'变为0。  
{
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
		{
			if (a[i][j] == '.')
			{
				p[i][j] = 0;
			}
			else if (57 >= int(a[i][j]) && int(a[i][j]) >= 49)
			{
				p[i][j] = (a[i][j] - '0');
			}
			else
			{
				cout << "该数独题目不符合要求，请检查后重新输入。" << endl;
				system("pause");
			}
		}
}

bool  Inspection(int sudo[9][9])
{
	int temp[10] = { 0,0,0,0,0,0,0,0,0,0 };
	int i, j, m, n;
	for (i = 0; i < 9; i++)
		for (j = 0; j < 9; j++)
			if (sudo[i][j] != 0)
			{
				//检查所在行的元素是否重复  
				for (m = 0; m < 10; m++)
					temp[m] = 0;
				for (m = 0; m < 9; m++)
					if (sudo[i][m] != 0)
					{
						if (temp[sudo[i][m]] == 0)
							temp[sudo[i][m]] = 1;
						else
							return false;
					}
				//检查所在列数字是否合法  
				for (m = 0; m < 10; m++)
					temp[m] = 0;
				for (m = 0; m < 9; m++)
					if (sudo[m][j] != 0)
					{
						if (temp[sudo[m][j]] == 0)
							temp[sudo[m][j]] = 1;
						else
							return false;
					}
				//检查所在小九宫格中数字是否合法(i,j)与小九宫格到位置（i/3*3,j/3*3） 转换。  
				for (m = 0; m < 10; m++)
					temp[m] = 0;
				for (m = 0; m < 3; m++)
					for (n = 0; n < 3; n++)
						if (sudo[i / 3 * 3 + m][j / 3 * 3 + n] != 0)
						{
							if (temp[sudo[i / 3 * 3 + m][j / 3 * 3 + n]] == 0)
								temp[sudo[i / 3 * 3 + m][j / 3 * 3 + n]] = 1;
							else
								return false;
						}
			}
	return true;
}


int Blank_number(int sudo[9][9])                                     //计算所给数独中待填入的空白数  
{
	int i, j, num = 0;
	for (i = 0; i < 9; i++)
		for (j = 0; j < 9; j++)
			if (sudo[i][j] == 0)
				num++;
	return num;
}





void Initialization_col_row(int sudo[9][9], Node * node_sudo)
{
	int m = 0;
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
		{
			if (sudo[i][j] == 0)
			{
				(node_sudo + m)->col = i;
				(node_sudo + m)->row = j;
				m++;
			}
		}
}

int Find_value(int sudo[9][9], Node * node_sudo)                                //找到合法的解。   value[10],第一个值存总共可以由多少个元素。 可以取得值value=0，否则=1。  
{
	int m, n, i = node_sudo->col, j = node_sudo->row;

	for (m = 0; m < 10; m++)
		node_sudo->value[m] = 0;
	for (m = 1; m < 10; m++)
	{
		node_sudo->value[sudo[i][m - 1]] = 1;                  //筛选行方向的值  
		node_sudo->value[sudo[m - 1][j]] = 1;                  //筛选列方向的值  
	}
	for (m = 0; m < 3; m++)                                    //筛选小九宫格方向的值  
		for (n = 0; n < 3; n++)
			node_sudo->value[sudo[i / 3 * 3 + m][j / 3 * 3 + n]] = 1;

	node_sudo->value[0] = 0;                                           //node->value[0]记录候选值个数，前面的循环可能会修改掉它，需要重新赋0值  
	for (m = 1; m < 10; m++)
		if (node_sudo->value[m] == 0)  node_sudo->value[0]++;


	for (m = 1; m < 10; m++)                                               //找到第一个可以取的值////////////////////////////////////////  
		if (node_sudo->value[m] == 0)
		{
			node_sudo->value[m] = 1;
			node_sudo->value[0]--;
			break;
		}

	//返回候选值m，若无候选值可用，返回错误标记-1  
	if (m == 10)
		return -1;
	else
		return m;
}




void  Solving(int sudo[9][9], int num_of_empty, Node* node_sudo)               //num_of_empty  为总共空格数。  
{
	int k = 0;       //记录已经求得了几个解。  
	int number = 1;  //从第一个空格数开始求解。  
	while (0 < number && number <= (num_of_empty + 1))
	{
		int i = (node_sudo + (number - 1))->col;
		int j = (node_sudo + (number - 1))->row;

		if (number == 50)
		{
			int a = 0;
			a++;
		}
		if (number == 61)
		{	
			int a = 0;
			a++;
		}

		if (number > num_of_empty)
		{
			k++; int count = 0;
			for (int i = 0; i < num_of_empty; i++)
			{
				if ((node_sudo + i)->value[0] == 0) { count++; }
			}
			//////////第一种情况//////////////////////////////////// 最后一次试探 刚好是得到所有解。提前结束  
			if (count == num_of_empty)
			{
				cout << "这是第" << k << "个答案：" << endl;
				Print_sudo(sudo);
				cout << "已经得到所有答案" << endl;
				number++;
			}
			else if (count != num_of_empty)                    //向前回溯求解。。。  
			{
				cout << "这是第" << k << "个答案：" << endl;
				Print_sudo(sudo);
				--number;
			}
		}
		else if (0 < number  &&  number <= num_of_empty)
		{

			if (sudo[i][j] != 0)
			{
				if ((node_sudo + (number - 1))->value[0] == 0)
				{
					sudo[i][j] = 0;
					(--number);
				}
				else if ((node_sudo + (number - 1))->value[0] != 0)
				{
					for (int index = 1; index < 10; index++)
					{
						if ((node_sudo + (number - 1))->value[index] == 0)
						{
							sudo[i][j] = index;
							(node_sudo + (number - 1))->value[index] = 1;
							(node_sudo + (number - 1))->value[0]--;
							break;
						}
					}
					(++number);

				}



			}
			else if (sudo[i][j] == 0)
			{
				sudo[i][j] = Find_value(sudo, (node_sudo + number - 1));
				if (sudo[i][j] == -1)
				{
					sudo[i][j] = 0;
					(--number);
				}
				else if (sudo[i][j] != -1)
				{
					(++number);
				}
			}
		}
	}

	if (number <= 0)
	{
		if (k == 0) { cout << "该数独没有解" << endl; }

		if (k != 0) { cout << "已得到该数独的所有解" << endl; }

	}
}

void Print_sudo(int sudo[9][9])
{
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
		{
			cout << sudo[i][j] << "  ";
			if (j % 8 == 0 && j != 0)
			{
				cout << endl;
			}
		}
}