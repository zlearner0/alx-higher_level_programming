#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome
 * @head: pointer to head of list
 * Return: 0 or 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
int range, i = 0;
listint_t *current = *head;
int count = 0;
while (current)
{
count++;
current = current->next;
}
if (!count || !current)
return (1);
int *arr = malloc(sizeof(int) * count);
if (!arr)
return (0);
current = *head;
while (current)
{
arr[i] = current->n;
i++;
current = current->next;
}
for (i = 0; i < count; i++)
range = count / 2;
i = 0;
while (i < range)
{
if (arr[i] != arr[count - 1 - i])
return (0);
i++;
}
free(arr);
return (1);
}
