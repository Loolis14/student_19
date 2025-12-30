/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_and_push_operations.c                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:07:30 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/30 23:57:18 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	swap(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

void	swap_one(t_deque *deque)
{
	if (deque->length < 2)
	{
		return ;
	}
	swap(&deque->numbers[(deque->front) % deque->capacity], &deque->numbers[(deque->front + 1) % deque->capacity]);
	write(1, "s", 1);
	write(1, &deque->tag, 1);
	write(1, "\n", 1);
	return ;
}

void	swap_both(t_deque *a, t_deque *b)
{
	swap(&a->numbers[a->front], &a->numbers[(a->front + 1) % a->capacity]);
	swap(&b->numbers[b->front], &b->numbers[(b->front + 1) % b->capacity]);
	write(1, "ss\n", 3);
	return ;
}

void	push_queue(t_deque *to_push, t_deque *to_pop)
{
	int	first_element_to_pop;

	if (to_pop->length == 0)
	{
		return ;
	}
	first_element_to_pop = pop_front(to_pop);
	push_front(to_push, first_element_to_pop);
	write(1, "p", 1);
	write(1, &to_push->tag, 1);
	write(1, "\n", 1);
}
