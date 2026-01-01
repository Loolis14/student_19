/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_3.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 13:54:34 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/31 11:28:17 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	position_max(t_deque *deque)
{
	if (deque_at(deque, 0) >= deque_at(deque, 1)
		&& deque_at(deque, 0) >= deque_at(deque, 2))
	{
		return (0);
	}
	return (1);
}

void	sort_3(t_deque *deque)
{
	int	index_max;

	index_max = position_max(deque);
	if (index_max == 0 && deque_at(deque, 1) <= deque_at(deque, 2))
	{
		rotate_one(deque);
	}
	else if (deque_at(deque, 0) >= deque_at(deque, 1))
	{
		swap_one(deque);
		if (deque_at(deque, 0) >= deque_at(deque, 2))
		{
			reverse_rotate_one(deque);
		}
	}
	else if (deque_at(deque, 0) <= deque_at(deque, 1)
		&& deque_at(deque, 1) >= deque_at(deque, 2))
	{
		reverse_rotate_one(deque);
		if (deque_at(deque, 0) >= deque_at(deque, 1))
		{
			swap_one(deque);
		}
	}
}
