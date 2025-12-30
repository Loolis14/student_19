/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algorithm_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 20:12:56 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/30 21:30:10 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stddef.h>
#include <stdlib.h>
#include <unistd.h>

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

size_t	ft_abs(ssize_t n)
{
	if (n < 0)
	{
		return (-n);
	}
	return (n);
}

ssize_t	number_of_rotations(size_t index, size_t length) //find direction + count
{
    if (index <= (length - 1) / 2)
    {
        return (index);
    }
    return (index - length);
}

size_t	calculate_cost(size_t index_of_b, size_t index_of_a, size_t length_a, size_t length_b)
{
	size_t	cost;
	ssize_t	rotation_a;
	ssize_t	rotation_b;
	size_t	ra;
	size_t	rb;

	cost = 0;
	rotation_a = number_of_rotations(index_of_a, length_a);
	rotation_b = number_of_rotations(index_of_b, length_b);
	ra = ft_abs(rotation_a);
	rb = ft_abs(rotation_b);
	if (rotation_a > 0 && rotation_b > 0)
		cost = (ft_max(rb, ra) - ft_min(rb, ra)) + ft_min(rb, ra);
	else if (rotation_a < 0 && rotation_b < 0)
		cost = (ft_max(ra, rb) - ft_min(ra, rb)) + ft_min(ra, rb) + 1;
	else
	{
		cost = ra + rb;
	}
	return (cost);
}

size_t	limits_idx_value(t_deque *deque, char c)
{
	size_t	i;
	limits	extrema;

	extrema.max = deque_at(deque, 0);
	extrema.index_max = 0;
	extrema.min = deque_at(deque, 0);
	extrema.index_min = 0;
	i = 1;
	while (i < deque->length)
	{
		if (deque_at(deque, i) > extrema.max)
		{
			extrema.max = deque_at(deque, i);
			extrema.index_max = i;
		}
		else if (deque_at(deque, i) < extrema.min)
		{
			extrema.min = deque_at(deque, i);
			extrema.index_min = i;
		}
		++i;
	}
	if (c == '+')
		return (extrema.index_max);
	else
		return(extrema.index_min);
}
