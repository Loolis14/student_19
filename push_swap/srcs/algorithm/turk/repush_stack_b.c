/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   repush_stack_b.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 14:32:41 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/31 11:27:56 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <limits.h>

static ssize_t	find_closest_bigger(int b_number, t_deque *a)
{
	int		value;
	int		closest_bigger;
	size_t	i;
	ssize_t	idx_of_closest_bigger;

	idx_of_closest_bigger = -1;
	closest_bigger = INT_MAX;
	i = 0;
	while (i < a->length)
	{
		value = deque_at(a, i);
		if (value > b_number && value <= closest_bigger)
		{
			closest_bigger = value;
			idx_of_closest_bigger = i;
		}
		++i;
	}
	return (idx_of_closest_bigger);
}

void	repush_stack_b(t_deque *a, t_deque *b)
{
	ssize_t		idx_clst_bigger;
	ssize_t		count_rotation;

	while (b->length > 0)
	{
		idx_clst_bigger = find_closest_bigger(b->numbers[b->front], a);
		if (idx_clst_bigger == -1)
		{
			idx_clst_bigger = limits_idx_value(a, '-');
		}
		count_rotation = number_of_rotations(idx_clst_bigger, a->length);
		if (count_rotation != 0)
			rotate_by_one(a, count_rotation);
		push_queue(a, b);
	}
}
