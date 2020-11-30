#include "sort.h"

void heapify(int *array, int size, int iterator);
void swap(int *a, int *b);

void heap_sort(int *array, size_t size)
{
	int iterator;

	for (iterator = (size / 2) - 1; iterator >= 0; iterator--)
	{
		heapify(array, size, iterator);
		print_array(array, size);
	}
		
    
    for (iterator = size - 1; iterator >= 0; iterator--)
	{
		swap(&array[0], &array[iterator]);
		heapify(array, iterator, 0);
		print_array(array, size);
	}
}

void heapify(int *array, int size, int iterator)
{
    int max = iterator;
    int left_child = (2 * iterator) + 1;
    int rigth_child = (2 * iterator) + 2;

    if (left_child < size && array[left_child] > array[max])
        max = left_child;
    
    if (left_child < size && array[rigth_child] > array[max])
        max = left_child;
    
    if (max != iterator)
    {
        swap(&array[iterator], &array[max]);
        heapify(array, size, max);
    }
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}