#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - function that reverses given linked list
 * @head: Pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * compare_lists - function that compares two linked lists
 * @list1: First linked list
 * @list2: Second linked list
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	return (list1 == NULL && list2 == NULL);
}
/**
 * is_palindrome - funct that checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			second_half = slow->next;
		}
		else
		{
			second_half = slow;
		}

		prev_slow->next = NULL;
		reverse_list(&second_half);
		is_palindrome = compare_lists(*head, second_half);

		reverse_list(&second_half);

		if (fast != NULL)
		{
			prev_slow->next = slow;
			slow->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}
	return (is_palindrome);
}
