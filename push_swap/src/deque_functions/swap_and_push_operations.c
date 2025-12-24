/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_and_push_operations.c                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:07:30 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/23 22:31:09 by mmeurer          ###   ########.fr       */
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
	swap(&deque->numbers[deque->front], &deque->numbers[(deque->front + 1) % deque->capacity]);
	if (deque->cost_calcul == false)
		printf("%c%c\n", 's', deque->tag);
	return ;
}

void	swap_both(t_deque *a, t_deque *b)
{
	swap(&a->numbers[a->front], &a->numbers[(a->front + 1) % a->capacity]);
	swap(&b->numbers[b->front], &b->numbers[(b->front + 1) % b->capacity]);
	if (a->cost_calcul == false || b->cost_calcul == false)
		write(1, "ss", 2);
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
	if (to_push->cost_calcul == false || to_pop->cost_calcul == false)
		printf("%c%c\n", 'p', to_push->tag);
}
