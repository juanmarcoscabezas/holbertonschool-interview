#include "search_algos.h"

void print_array(int *array, int start, int end);

int advanced_binary(int *array, size_t size, int value)
{
	int first = 0, last = size;
	int middle = (first + last - 1) / 2;

	while (first <= last) {
		print_array(array, first, last);
		if (array[middle] < value)
			first = middle + 1;
		else if (array[middle] == value) {
			return (middle + 1);
		}
		else
			last = middle - 1;
		
		middle = (first + last) / 2;
	}
	return (-1);
}

void print_array(int *array, int start, int end)
{
	int iterator;

	printf("Searching in array:");
	for (iterator = start; iterator < end; iterator++)
	{
		printf(", %d", array[iterator]);
	}
	putchar('\n');
}