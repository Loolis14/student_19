#include "push_swap.h"
#include <stddef.h>
#include <stdlib.h>

size_t	find_closest_smaller(int number, t_deque *b)
{
	size_t	i;
	size_t	index_b;
	int		tmp_number_in_b;

	i = 0;
	index_b = 0;
	while (i < b->length)
	{
		if (deque_at(b, i) < number)
		{
			tmp_number_in_b = deque_at(b, i);
			index_b = i;
			++i;
			break ;
		}
		++i;
	}
	while (i < b->length)
	{
		if (deque_at(b, i) < number && deque_at(b, i) > tmp_number_in_b)
		{
			tmp_number_in_b = deque_at(b, i);
			index_b = i;
		}
		++i;
	}
	return (index_b);
}

size_t	find_index_of_closest_b(t_deque *a, t_deque *b, t_target *target)
{
	size_t	i;
	size_t	tmp_idx_closest;
	size_t	tmp_cost;

	i = 0;

	while(i < a ->length)
	{
		tmp_idx_closest = find_closest_smaller(deque_at(a, i), b);
		tmp_cost = calculate_cost(tmp_idx_closest, i, a->length, b->length);
		if (tmp_cost == 0)
		{
			target->index_a = i;
			target->number_in_a = deque_at(a, i);
			break ;
		}
		else 
		{
			if (i == 0 || tmp_cost < target->cost)
			{
				target->cost = tmp_cost;
				target->index_b = tmp_idx_closest;
				target->index_a = i;
				target->number_in_a = deque_at(a, i);
			}
		}
		++i;
		target->number_in_b = b->numbers[target->index_b];
	}
	return (0); //a voir ce que je veux return;
}

void	push_to_top(t_deque *a, t_deque *b, t_target *target)
{
	if (target->cost == 0)
	{
		push_queue(b, a);
	}
}

void	sort_stack_a(t_deque *a, t_deque *b)
{
	t_target	*target;

	target = malloc(sizeof(t_target));
	if (target == NULL)
	{
		return ;
	}
	while(a->length > 3)
	{
		find_index_of_closest_b(a, b, target); //target de rempli avec nombre en a et son index, nombre de b et son index.
		push_to_top(a, b, target);
		break ;
	}
	sort_3(a);
	printf("number dans a %i\n", target->number_in_a);
	printf("number dans b %i\n", target->number_in_b);
	printf("index a : %zi\n", target->index_a);
	printf("index b : %zi\n", target->index_b);
	printf("cout : %zi\n", target->cost);
}
