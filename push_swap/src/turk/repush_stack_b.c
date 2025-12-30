/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   repush_stack_b.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 14:32:41 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/30 21:08:36 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stddef.h>
#include <stdlib.h>
#include <unistd.h>

static ssize_t	find_closest_bigger(int b_number, t_deque *a)
{
	size_t	i;
	ssize_t	index_a;
	int		tmp_number_in_a;

	i = 0;
	index_a = -1;
	while (i < a->length)
	{
		if (deque_at(a, i) > b_number)
		{
			tmp_number_in_a = deque_at(a, i);
			index_a = i;
			++i;
			break ;
		}
		++i;
	}
	while (i < a->length)
	{
		if (deque_at(a, i) > b_number && deque_at(a, i) < tmp_number_in_a)
		{
			tmp_number_in_a = deque_at(a, i);
			index_a = i;
		}
		++i;
	}
	return (index_a);
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
