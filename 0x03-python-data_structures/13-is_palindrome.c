#include <stdio.h>
#include "lists.h"
/**
  * is_palindrome - checks if is palindrome
  *
  * @head: head of linked list
  * Return: Always 0 (Success)
  */
int is_palindrome(listint_t **head)
{
	listint_t *curr;
	int list[1024], y, x, i = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	curr = *head;
	while (curr != NULL)
	{
		list[i] = curr->n;
		curr = curr->next;
		i++;
	}
	for (y = 0, x = i - 1; y < i; y++, x--)
	{
		if (y == i / 2)
			break;
		if (list[y] != list[x])
			return (0);
	}
	return (1);
}
