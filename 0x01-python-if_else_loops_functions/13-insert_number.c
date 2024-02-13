#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head pointer
 * @number: data to be added
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *prv = NULL, *newNode = NULL;

	if (!head)
		return (NULL);
	newNode = malloc(sizeof(*newNode));
	if (!newNode)
		return (NULL);

	newNode->n = number, newNode->next = NULL;
	ptr = *head;
	if (!ptr)
	{
		*head = newNode;
		return (newNode);
	}

	while (ptr)
	{
		if (ptr->n >= number)
		{
			if (!prv)
				*head = newNode, newNode->next = ptr;
			else
				newNode->next = ptr, prv->next = newNode;
			return (newNode);
		}
		prv = ptr;
		ptr = ptr->next;
	}
	prv->next = newNode;
	return (newNode);
}
