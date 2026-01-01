/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate_operations.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:05:24 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/31 10:03:13 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rotate_one(t_deque *deque)
{
	int	first_element;

	first_element = pop_front(deque);
	push_back(deque, first_element);
	write(1, "r", 1);
	write(1, &deque->tag, 1);
	write(1, "\n", 1);
}

void	rotate_both(t_deque *a, t_deque *b)
{
	int	first_element_a;
	int	first_element_b;

	first_element_a = pop_front(a);
	first_element_b = pop_front(b);
	push_back(a, first_element_a);
	push_back(b, first_element_b);
	write(1, "rr\n", 3);
}

void	reverse_rotate_one(t_deque *deque)
{
	int	last_element;

	last_element = pop_back(deque);
	push_front(deque, last_element);
	write(1, "rr", 2);
	write(1, &deque->tag, 1);
	write(1, "\n", 1);
}

void	reverse_rotate_both(t_deque *a, t_deque *b)
{
	int	last_element_a;
	int	last_element_b;

	last_element_a = pop_back(a);
	last_element_b = pop_back(b);
	push_front(a, last_element_a);
	push_front(b, last_element_b);
	write(1, "rrr\n", 4);
}
