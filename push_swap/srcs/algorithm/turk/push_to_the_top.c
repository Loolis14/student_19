/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_to_the_top.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 14:32:32 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/31 11:28:02 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	to_the_top(t_deque *a, t_deque *b, t_target *target)
{
	ssize_t	rotation_a;
	ssize_t	rotation_b;

	if (target->cost == 0)
	{
		return ;
	}
	rotation_a = number_of_rotations(target->index_a, a->length);
	rotation_b = number_of_rotations(target->index_b, b->length);
	while (rotation_a > 0 && rotation_b > 0)
	{
		rotate_both(a, b);
		rotation_a -= 1;
		rotation_b -= 1;
	}
	while (rotation_a < 0 && rotation_b < 0)
	{
		reverse_rotate_both(a, b);
		rotation_a += 1;
		rotation_b += 1;
	}
	rotate_by_one(a, rotation_a);
	rotate_by_one(b, rotation_b);
}
