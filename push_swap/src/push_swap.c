/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 17:39:20 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/31 00:01:03 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stdlib.h>

int	ft_free(t_deque *deque)
{
	free(deque->numbers);
	free(deque);
	return (0);
}

int	main(int argc, char **argv)
{
	ssize_t	count;
	t_deque	*a;
	t_deque	*b;

	if (argc == 1 || argv[1][0] == '\0')
		return (0);
	count = count_numbers(argv + 1);
	if (count == -1 || count == 0)
	{
		write(1, "Error\n", 6);
		return (0);
	}
	a = create_t_deque(count, 'a');
	if (!parse_numbers(argv + 1, a) || !check_duplicate(a))
	{
		write(1, "Error\n", 6);
		return (ft_free(a));
	}
	if (!is_sorted(a))
	{
		b = create_t_deque(count, 'b');
		dispatch_by_length(a, b);
		ft_free(b);
	}
	return (ft_free(a));
}
