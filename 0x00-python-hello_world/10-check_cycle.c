#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0 if no cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		printf("list has no loop\n");
		return (0);
	}

	slow = list->next;
	fast = list->next->next;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast  = fast->next->next;
		if (slow == fast)
		{
			printf("Linked List contains a loop\n");
			return (1);
		}
	}
	return (0);
}
