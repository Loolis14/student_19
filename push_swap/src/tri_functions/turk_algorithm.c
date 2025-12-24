#include "push_swap.h"
#include <stddef.h>

size_t	ft_min(size_t a, size_t b)
{
	if (a <= b)
	{
		return (a);
	}
	return (b);
}

size_t	ft_max(size_t a, size_t b)
{
	if (a > b)
	{
		return (a);
	}
	return (b);
}

size_t	calculate_cost(size_t index_of_b, size_t index_of_a, size_t length_a, size_t length_b)
{
	size_t	cost;
	size_t	middle_a;
	size_t	middle_b;
	size_t	left_a;
	size_t	left_b;

	cost = 0;
	middle_a = length_a / 2;
	middle_b = length_b / 2;
	if (index_of_b <= middle_b && index_of_a <= middle_a)
		cost = (ft_max(index_of_b, index_of_a) - ft_min(index_of_b, index_of_a)) + ft_min(index_of_b, index_of_a);
	else if (index_of_b > middle_b && index_of_a > middle_a)
	{
		left_a = length_a - index_of_a;
		left_b = length_b - index_of_b;
		cost = (ft_max(left_a, left_b) - ft_min(left_a, left_b)) + ft_min(left_a, left_b) + 1;
	}
	else
	{
		if (index_of_b <= middle_b)
			cost = index_of_b + (length_a - index_of_a) + 1;
		else 
			cost = index_of_a + (length_b - index_of_b) + 1;
	}
	return (cost);
}

void	turk_algorithm(t_deque *a, t_deque *b)
{
	push_queue(b, a);
	push_queue(b, a);

	//parcours des nombres dans a, un par un jusqu'à ce qu'il n'en reste que 3
		//chercher le plus proche petit dans b; ok
		//calcul du cout;						ok
		//fais les opérations
		//push a -> b;
	
	sort_stack_a(a, b);

	//sort 3
	//sort_3(a);

	//parcours des nombres dans b, un par un jusqu'à ce qu'il n'en reste plus dans b
		//chercher le plus petit_grand dans a;
		//calcul du cout;
		//fais les opérations
		//push b -> a;
}
