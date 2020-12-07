#include "search_algos.h"

void print_array(int *array, int start, int end);

int advanced_binary(int *array, size_t size, int value)
{
	int first = 0, last = size - 1;
	int middle = (first + last) / 2;

	if (!array)
		return (-1);

	while (first <= last)
	{
		print_array(array, first, last);
		if (array[middle] < value)
			first = middle + 1;
		else
			last = middle - 1;
		if (array[middle] == value)
			return (middle);

		middle = (first + last) / 2;
	}
	return (-1);
}

void print_array(int *array, int start, int end)
{
	int iterator;

	printf("Searching in array: ");
	for (iterator = start; iterator <= end; iterator++)
	{
		if (iterator != start)
			printf(", ");
		printf("%d", array[iterator]);
	}
	putchar('\n');
}
