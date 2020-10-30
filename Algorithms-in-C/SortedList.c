#include <stdio.h>
#include <stdlib.h>

typedef struct SortedList
{
	int value;
	struct SortedList *next;
}SortedList;

void PrintList(SortedList *list)
{
	while(list != NULL)
	{
		printf("%d ", list->value);
		list = list->next;
	}
	printf("\n");
}

SortedList *InsertAfter(int value, SortedList *list)
{
	SortedList *new = (SortedList*)malloc(sizeof(SortedList));
	new->value = value;

	if(list == NULL)
	{
		new->next = NULL;
		list = new;
		return list;
	}
	SortedList *p = list;
	while(p->next != NULL)
	{
		p = p->next;
	}
	new->next = NULL;
	p->next = new;

	return list;
}

SortedList *SortList(SortedList *list)
{
	SortedList *new_list = NULL;
	SortedList *p = list;

	while(p != NULL)
	{
		if(new_list == NULL) // cazul in care lista este goala
		{
			SortedList *new = (SortedList*)malloc(sizeof(SortedList));
			new->value = p->value;
			new->next = NULL;
			new_list = new;
		}
		else
		{
			SortedList *p2 = new_list;

			while(p2->next !=  NULL && p2->next->value < p->value)
			{
				p2 = p2->next;
			}
			if(p2->next == NULL)
			{
				if(p2->value <= p->value) // cazul in care trebuie inserat la sfarsitul listei
				{		
					SortedList *new = (SortedList*)malloc(sizeof(SortedList));
					new->value = p->value;

					new->next = NULL;
					p2->next = new;
				}
				else // cazul in care lista are un element si trebuie inserat la inceput
				{
					SortedList *new = (SortedList*)malloc(sizeof(SortedList));
					new->value = p->value;

					new->next = new_list;
					new_list = new;
				}
			}
			else
			{
				if(new_list->value >= p->value) // cazul in care lista are mai multe elemente si trebuie inserat la inceput
				{
					SortedList *new = (SortedList*)malloc(sizeof(SortedList));
					new->value = p->value;

					new->next = new_list;
					new_list = new;
				}
				else
				{
					SortedList *new = (SortedList*)malloc(sizeof(SortedList)); // cazul in care trebuie inserat in interiorul listei
					new->value = p->value;

					new->next = p2->next;
					p2->next = new;
				}
			}
		}
		PrintList(new_list);
		p = p->next;
	}

	return new_list;
}

int main()
{
	SortedList *list;

	list = InsertAfter(5, list);
	list = InsertAfter(3, list);
	list = InsertAfter(21, list);
	list = InsertAfter(17, list);
	list = InsertAfter(4, list);

	PrintList(list);
	list = SortList(list);
	PrintList(list);

	return 0;
}