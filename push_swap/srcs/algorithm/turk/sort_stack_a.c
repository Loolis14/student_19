/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_stack_a.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 14:32:46 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/31 11:27:44 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stddef.h>
#include <stdlib.h>
#include <limits.h>

static ssize_t	find_closest_smaller(int a_number, t_deque *b)
{
	int		value;
	int		closest_smaller;
	size_t	idx_closest_smaller;
	size_t	i;

	idx_closest_smaller = -1;
	closest_smaller = INT_MIN;
	i = 0;
	while (i < b->length)
	{
		value = deque_at(b, i);
		if (value < a_number && value > closest_smaller)
		{
			closest_smaller = value;
			idx_closest_smaller = i;
		}
		++i;
	}
	return (idx_closest_smaller);
}

static void	find_cheaper(t_deque *a, t_deque *b, t_target *target)
{
	size_t	i;
	ssize_t	tmp_idx_closest;
	size_t	tmp_cost;

	i = 0;
	while (i < a ->length)
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
	while (a->length > 3)
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
