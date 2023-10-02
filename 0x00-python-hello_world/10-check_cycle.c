#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @h: pointer to head of list
 * return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (slow && fast)
	{
		if (!fast->next)
			break;
		slow = slow->next;
		fast = fast->next->next;
		if (slow && fast == slow)
			return (1);
	}
	return (0);
}
