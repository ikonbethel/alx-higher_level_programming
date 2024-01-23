#include "lists.h"
#include <unistd.h>

int check_size(listint_t **head);
listint_t *reverse_list(listint_t **head);

/**
 *reverse_list - Reverses a linked list
 *@head: Pointer to a pointer to the head of a linked list
 * Return: Reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current, *previous, *next;

	if (!*head || *head == NULL)
		return (NULL);
	current = *head;
	previous = NULL;
	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
	return (*head);
}
/**
 *check_size - this Checks the size of a listint_t linked list
 *@head: the pointer to a pointer to the head of a linked list
 *Return: Size of linked list.
 */
int check_size(listint_t **head)
{
	listint_t *start = *head;
	int size = 0;

	if (start == NULL)
		return (0);

	while (start != NULL)
	{
		size++;
		start = start->next;
	}

	return (size);
}

/**
 * is_palindrome - this Checks if a linked list of integers is a palindrome.
 * @head: the Pointer to a pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *start, *left, *right, *mid;
	int size, i;

	if ((*head) == NULL || (*head)->next == NULL)
		return (1);

	start = *head;
	right = *head;
	size = check_size(&start);
	for (i = 1; i < size / 2; i++)
	{
		start = start->next;
	}
	if (size % 2 == 0 && start->n != start->next->n)
		return (0);
	left = reverse_list(&right);
	mid = left;
	i = 0;
	while (i < size / 2)
	{
		if (right->n != left->n)
			return (0);
		right = right->next;
		left = left->next;
		i++;
	}
	reverse_list(&mid);

	return (1);
}
