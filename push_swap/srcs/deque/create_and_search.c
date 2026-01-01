/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   primitive_functions.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:07:21 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/30 20:45:22 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stdlib.h>

t_deque	*create_t_deque(int count, char tag)
{
	t_deque	*deque;

	deque = malloc(sizeof(t_deque));
	if (deque == NULL)
	{
		return (NULL);
	}
	deque->numbers = malloc(sizeof(int) * count);
	if (deque->numbers == NULL)
	{
		return (NULL);
	}
	deque->front = 0;
	deque->capacity = count;
	deque->length = 0;
	deque->tag = tag;
	return (deque);
}

int	deque_at(t_deque *deque, size_t i)
{
	return (deque->numbers[(deque->front + i) % deque->capacity]);
}
