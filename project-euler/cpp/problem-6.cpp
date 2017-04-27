// Problem6.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <stdio.h>
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	double nSumSquare = 0;
	double nSquareSum = 0;
	double nAnswer = -1;

	for(double k=1; k<=100; k++)
	{
		nSumSquare += pow(k, (int) 2);
		nSquareSum += k;
	}

	nSquareSum = pow(nSquareSum, (int) 2);
	nAnswer = nSquareSum - nSumSquare;

	printf("nSumSquare: %f", nSumSquare);
	printf("\nnSquareSum: %f", nSquareSum);
	printf("\nAnswer: %f", nAnswer);

	cin.get();
	return 0;
}
