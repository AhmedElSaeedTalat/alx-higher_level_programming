#include "lists.h"
/**
  * check_cycle - checks if there is a cycle
  *
  * @list: linked list passed to the function
  *
  * Return: 1 if there is a cycle 0 if there isn't
  */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptr2;

	if (list == NULL)
		return (0);
	ptr = ptr2 = list;
	while (ptr2 != NULL)
	{
		ptr2 = ptr2->next->next;
		ptr = ptr->next;
		if (ptr2 == ptr)
			return (1);
	}
	return (0);
}
