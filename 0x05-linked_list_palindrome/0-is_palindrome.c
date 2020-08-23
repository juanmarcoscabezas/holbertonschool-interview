#include "lists.h"

/**
 * is_palindrome - Finds if a linked list is a palindrome
 * @head: Head of the Linked list
 * Return: 0 if it is nota palidrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *iterator = *head;

	if (!iterator)
		return (1);

	while (iterator)
	{
		iterator = iterator->next;
	}
	return (1);
}
