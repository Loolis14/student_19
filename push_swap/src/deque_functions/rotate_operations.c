/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate_operations.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:05:24 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/23 22:28:18 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stdbool.h>

void	rotate_one(t_deque *deque)
{
	int	first_element;

	first_element = pop_front(deque);
	push_back(deque, first_element);
	if (deque->cost_calcul == false)
		printf("%c%c\n", 'r', deque->tag);
}

void	rotate_both(t_deque *a, t_deque *b)
{
	int	first_element_a;
	int	first_element_b;

	first_element_a = pop_front(a);
	first_element_b = pop_front(b);
	push_back(a, first_element_a);
	push_back(b, first_element_b);
	if (a->cost_calcul == false || b->cost_calcul == false)
		write(1, "rr", 2);
}

void	reverse_rotate_one(t_deque *deque)
{
	int	last_element;

	last_element = pop_back(deque);
	push_front(deque, last_element);
	if (deque->cost_calcul == false)
		printf("%s%c\n", "rr", deque->tag);
}

void	reverse_rotate_both(t_deque *a, t_deque *b)
{
	int	last_element_a;
	int	last_element_b;

	last_element_a = pop_back(a);
	last_element_b = pop_back(b);
	push_front(a, last_element_a);
	push_front(b, last_element_b);
	if (a->cost_calcul == false || b->cost_calcul == false)
		printf("%s\n", "rrr");
}
