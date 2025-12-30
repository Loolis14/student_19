/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_stack_a.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 14:32:46 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/30 21:03:00 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stddef.h>
#include <stdlib.h>

static ssize_t	find_closest_smaller(int a_number, t_deque *b)
{
	size_t	i;
	ssize_t	index_b;
	int		tmp_number_in_b;

	i = 0;
	index_b = -1;
	while (i < b->length)
	{
		if (deque_at(b, i) < a_number)
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
		if (deque_at(b, i) < a_number && deque_at(b, i) > tmp_number_in_b)
		{
			tmp_number_in_b = deque_at(b, i);
			index_b = i;
		}
		++i;
	}
	return (index_b);
}

static void	find_cheaper(t_deque *a, t_deque *b, t_target *target)
{
	size_t	i;
	ssize_t	tmp_idx_closest;
	size_t	tmp_cost;

	i = 0;
	while(i < a ->length)
	{
		tmp_idx_closest = find_closest_smaller(deque_at(a, i), b);
		if (tmp_idx_closest == -1)
		{
			tmp_idx_closest = limits_idx_value(b, '+');
		}
		tmp_cost = calculate_cost(tmp_idx_closest, i, a->length, b->length);
		if (tmp_cost == 0)
			break ;
		else if (i == 0 || tmp_cost < target->cost)
		{
			target->cost = tmp_cost;
			target->index_a = i;
			target->index_b = tmp_idx_closest;
		}
		++i;
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
		target->cost = ft_max(a->length, b->length);
		target->index_a = 0;
		target->index_b = 0;
		find_cheaper(a, b, target);
		to_the_top(a, b, target);
		push_queue(b, a);
	}
	free(target);
}
