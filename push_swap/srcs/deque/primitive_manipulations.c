/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   deque_manipulations.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:05:38 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/23 12:07:49 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push_front(t_deque *deque, int value)
{
	deque->front = (deque->front + deque->capacity - 1) % deque->capacity;
	deque->numbers[deque->front] = value;
	++deque->length;
}

void	push_back(t_deque *deque, int value)
{
	int	rear;

	rear = (deque->front + deque->length) % deque->capacity;
	deque->numbers[rear] = value;
	++deque->length;
}

int	pop_front(t_deque *deque)
{
	int	value;

	value = deque->numbers[deque->front];
	deque->front = (deque->front + 1) % deque->capacity;
	--deque->length;
	return (value);
}

int	pop_back(t_deque *deque)
{
	int	value;
	int	rear;

	rear = (deque->front + deque->length - 1) % deque->capacity;
	value = deque->numbers[rear];
	--deque->length;
	return (value);
}
