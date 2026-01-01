/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_2.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 10:13:09 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/31 11:40:48 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rotate_by_one(t_deque *stack, ssize_t rotations)
{
	while (rotations > 0)
	{
		rotations -= 1;
		rotate_one(stack);
	}
	while (rotations < 0)
	{
		rotations += 1;
		reverse_rotate_one(stack);
	}
}

size_t	limits_idx_value(t_deque *stack, char c)
{
	size_t		i;
	int			value;
	t_limits	extrema;

	value = deque_at(stack, 0);
	extrema = (t_limits){value, 0, value, 0};
	i = 1;
	while (i < stack->length)
	{
		value = deque_at(stack, i);
		if (value > extrema.max)
		{
			extrema.max = value;
			extrema.index_max = i;
		}
		else if (value < extrema.min)
		{
			extrema.min = value;
			extrema.index_min = i;
		}
		++i;
	}
	if (c == '+')
		return (extrema.index_max);
	return (extrema.index_min);
}
