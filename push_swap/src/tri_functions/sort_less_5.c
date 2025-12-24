#include "push_swap.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

limits	find_limits(t_deque *a)
{
	size_t	i;
	limits	extrema;

	extrema.max = deque_at(a, 0);
	extrema.index_max = 0;
	extrema.min = deque_at(a, 0);
	extrema.index_min = 0;
	i = 1;
	while (i < a->length)
	{
		if (deque_at(a, i) > extrema.max)
		{
			extrema.max = deque_at(a, i);
			extrema.index_max = i;
		}
		else if (deque_at(a, i) < extrema.min)
		{
			extrema.min = deque_at(a, i);
			extrema.index_min = i;
		}
		++i;
	}
	return (extrema);
}

void	sort_4(t_deque *a, t_deque *b)
{
	limits	extrema;

	extrema = find_limits(a);
	if (extrema.index_max == 0 || extrema.index_min == 0)
	{
		push_queue(b, a);
		sort_3(a);
		push_queue(a,b);
	}
	else if (extrema.index_max == (a->length - 1) || extrema.index_min == (a->length - 1))
	{
		reverse_rotate_one(a);
		push_queue(b, a);
		sort_3(a);
		push_queue(a,b);
	}
	else 
	{
		swap_one(a);
		push_queue(b, a);
		sort_3(a);
		push_queue(a,b);
	}
	if (a->numbers[a->front] == extrema.max)
	{
		rotate_one(a);
	}
}

void	sort_5(t_deque *a, t_deque *b)
{
	limits	extrema;

	extrema = find_limits(a);
	if (extrema.index_max <= 1 && extrema.index_min <= 1)
	{
		push_queue(b, a);
		push_queue(b,a);
		sort_3(a);
	}
	else if (extrema.index_max > 2 && extrema.index_min > 2)
	{
		reverse_rotate_one(a);
		push_queue(b, a);
		reverse_rotate_one(a);
		push_queue(b,a);
		sort_3(a);
	}
	else if (extrema.index_max == 0 && extrema.index_min == (a->length - 1))
	{
		push_queue(b, a);
		reverse_rotate_one(a);
		push_queue(b, a);
		sort_3(a);
	}
	else 
	{
		turk_algorithm(a, b);

	}
	if (b->numbers[b->front] > b->numbers[b->front + 1])
	{
		push_queue(a, b);
		rotate_one(a);
		push_queue(a, b);
	}
	else
	{
		push_queue(a, b);
		push_queue(a, b);
		rotate_one(a);
	}	
}
