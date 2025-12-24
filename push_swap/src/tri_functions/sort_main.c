#include "push_swap.h"
#include <stddef.h>
#include <stdint.h>

void	dispatch_by_length(t_deque *a, t_deque *b)
{
	if (a->length == 1)
		return ;
	else if (a->length == 2)
	{
		swap_one(a);
		return ;
	}
	else if (a->length == 3)
		sort_3(a);
	else if (a->length == 4)
		sort_4(a, b);
	else if (a->length == 5)
		sort_5(a, b);
	else
	{
		turk_algorithm(a, b);
	}
}
