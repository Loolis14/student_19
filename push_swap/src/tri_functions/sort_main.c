/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_main.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 13:54:19 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/30 21:08:18 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	turk(t_deque *a, t_deque *b)
{
	size_t		idx_min;
	ssize_t		count_rotation;

	push_queue(b, a);
	push_queue(b, a);
	sort_stack_a(a, b);
	sort_3(a);
	repush_stack_b(a, b);
	if (!is_sorted(a))
	{
		idx_min = limits_idx_value(a, '-');
		count_rotation = number_of_rotations(idx_min, a->length);
		rotate_by_one(a, count_rotation);
	}
}

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
	else
	{
		turk(a, b);
	}
}
