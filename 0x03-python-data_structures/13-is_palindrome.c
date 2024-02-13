#include "lists.h"

/**
 * is_palindrome_rec - utility function
 * @front: pointer to head of list
 * @back: pointer to traverse with
 * @ans: tells if list is palindrome
 *
 * Return: void
 */
void is_palindrome_rec(listint_t **front, listint_t *back, int *ans)
{
	if (!back)
		return;
	is_palindrome_rec(front, back->next, ans);
	if ((*front)->n != back->n)
		*ans = 0;
	*front = (*front)->next;
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *front, *back;
	int ans;

	if (!head)
		return (1);
	front = *head, back = *head;
	if (!front)
		return (1);
	ans = 1;
	is_palindrome_rec(&front, back, &ans);
	return (ans);
}
