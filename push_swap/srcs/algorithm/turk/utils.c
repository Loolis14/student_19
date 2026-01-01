/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 20:12:56 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/31 10:21:07 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static size_t	ft_min(size_t a, size_t b)
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

static size_t	ft_abs(ssize_t n)
{
	if (n < 0)
	{
		return (-n);
	}
	return (n);
}

ssize_t	number_of_rotations(size_t index, size_t length)
{
	if (index <= (length - 1) / 2)
	{
		return (index);
	}
	return (index - length);
}

size_t	calculate_cost(size_t idx_b, size_t idx_a, size_t lgh_a, size_t lgh_b)
{
	size_t	cost;
	ssize_t	rotation_a;
	ssize_t	rotation_b;
	size_t	ra;
	size_t	rb;

	cost = 0;
	rotation_a = number_of_rotations(idx_a, lgh_a);
	rotation_b = number_of_rotations(idx_b, lgh_b);
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
