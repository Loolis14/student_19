#include "push_swap.h"

int	max(t_deque *deque)
{
	if (deque_at(deque, 0) >= deque_at(deque, 1) && deque_at(deque, 0) >= deque_at(deque, 2))
		return(0);
	return (1);
}

void	sort_3(t_deque *deque)
{
	int	index_max;

	//312 - ra				i - 1 > i < i + 1
	index_max = max(deque);
	if (index_max == 0 && deque_at(deque, 1) <= deque_at(deque, 2))
	{
		rotate_one(deque);
	}
	//321 - sa & rra		i - 1 > i > i + 1
	//213 - sa				i - 1 > i < i + 1
	else if (deque_at(deque, 0) >= deque_at(deque, 1))
	{
		swap_one(deque);
		if(deque_at(deque, 0) >= deque_at(deque, 2))
		{
			reverse_rotate_one(deque);
		}
	}
	//231 - rra				i - 1 < i > i + 1
	//132 - rra & sa		i - 1 < i > i + 1
	else if (deque_at(deque, 0) <= deque_at(deque, 1) && deque_at(deque, 1) >= deque_at(deque, 2))
	{
		reverse_rotate_one(deque);
		if(deque_at(deque, 0) >= deque_at(deque, 1))
		{
			swap_one(deque);
		}
	}
	//123 - nothing
}
