#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of head of list
 * @number: integer to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = *head, *current;

	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	current->n = number;

	if (new_node == NULL || new_node->n >= number)
	{
		current->next = new_node;
		*head = current;
		return (current);
	}

	while (new_node && new_node->next && new_node->next->n < number)
		new_node = new_node->next;

	current->next = new_node->next;
	new_node->next = current;

	return (current);
}
