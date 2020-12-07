#include "search_algos.h"

void print_array(int *array, int start, int end);

/**
 * advanced_binary - Binary search
 * @array: Array to make search
 * @size: Size of @array
 * @value: Value toi find
 * Return: Position of @value on @array on success, -1 otherwise
 */
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
			last = middle;
		if (array[first] == value)
			return (first);

		middle = (first + last) / 2;
	}
	return (-1);
}

/**
 * print_array - Print array
 * @array: Array to make search
 * @start: Position to start printing
 * @end: Position to end printing
 * Return:
 */
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
