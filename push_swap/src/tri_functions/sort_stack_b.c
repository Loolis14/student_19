#include "push_swap.h"

size_t	find_closest_bigger(int n, t_deque *a)
{
	size_t	i;
	size_t	index_closest_bigger;
	int		n_temp;

	i = 0;
	index_closest_bigger = 0;
	while (i < a->length)
	{
		if (deque_at(a, i) > n)
		{
				n_temp = deque_at(a, i);
				index_closest_bigger = i;
				break ;
		}
		++i;
	}
	while (i < a->length)
	{
		if (deque_at(a, i) > n && n < n_temp)
		{
				n_temp = deque_at(a, i);
				index_closest_bigger = i;
		}
		++i;
	}
	return (index_closest_bigger);
}
