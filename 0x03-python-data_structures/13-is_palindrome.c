#include "lists.h"

/**
 * reverse - Reverse a linked list.
 * @head_medium: Head of the linked list.
 * Return: void.
 */
void reverse(listint_t **head_medium)
{
	listint_t *current = *head_medium, *next = NULL, *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_medium = prev;
}

/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Head of the linked list.
 * Return: 1 if it is, 0 if doesn't.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *medium, *current;

	fast = *head;
	slow = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	medium = slow;
	reverse(&medium);
	current = *head;
	while (medium != NULL)
	{
		if (medium->n != current->n)
			return (0);

		medium = medium->next;
		current = current->next;
	}
	return (1);
}
