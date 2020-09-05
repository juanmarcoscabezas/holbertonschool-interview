#include "lists.h"

/**
 * check_cycle - Checks if a linked list is a circular one
 * @list: Linked list
 * Return: 0 if has not cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	while (tortoise && hare)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
