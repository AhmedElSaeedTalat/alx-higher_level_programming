#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
  * insert_node - insert a node in a sorted list
  *
  * @head: head of list passed
  *
  * @number: number to add to the newly created list
  * Return: address to the new Node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	new->next = NULL, new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	curr = *head;
	while (curr != NULL)
	{
		if (number < (*head)->n)
		{
			new->next = *head, *head = new;
			return (new);
		}
		else if ((curr->n < number) && (curr->next->n > number))
		{
			new->next = curr->next, curr->next = new;
			return (new);
		}
		curr = curr->next;
	}
	if (number > curr->n)
	{
		curr->next = new;
		return (new);
	}
	return (new);
}
