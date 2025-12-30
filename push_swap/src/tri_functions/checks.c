/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checks.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 13:54:38 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/30 13:54:39 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stdbool.h>

bool	is_sorted(t_deque *deque)
{
	size_t	i;

	i = 1;
	while (i < deque->length)
	{
		if (deque_at(deque, i - 1) > deque_at(deque, i))
		{
			return (false);
		}
		++i;
	}
	return (true);
}

bool	check_duplicate(t_deque *deque)
{
	size_t	i;
	size_t	j;

	i = 0;
	while (i < deque->length - 1)
	{
		j = i + 1;
		while (j < deque->length)
		{
			if (deque_at(deque, i) == deque_at(deque, j))
			{
				return (false);
			}
			++j;
		}
		++i;
	}
	return (true);
}
