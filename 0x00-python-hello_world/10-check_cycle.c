#include "lists.h"

/**
 * check_cycle - custom func to see whether the singly linked list has cycle
 * @list: singly linked list provided
 * Return: 1; true for present cycle, 0; false for no cycle found
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == 0)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
