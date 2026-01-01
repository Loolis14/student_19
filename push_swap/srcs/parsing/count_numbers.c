/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   count_numbers.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:10:31 by mmeurer           #+#    #+#             */
/*   Updated: 2026/01/01 22:38:12 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stddef.h>

int	is_digit(char c)
{
	return (c >= '0' && c <= '9');
}

int	is_space(char c)
{
	return (c == ' ' || (c >= '\t' && c <= '\r'));
}

ssize_t	count_numbers(char **argv)
{
	ssize_t	count;
	size_t	j;

	count = 0;
	while (*argv)
	{
		j = 0;
		while ((*argv)[j])
		{
			if ((((*argv)[j] == '+' || (*argv)[j] == '-') &&
				is_digit((*argv)[j + 1])) || (is_digit((*argv)[j])))
			{
				++j;
				++count;
				while (is_digit((*argv)[j]))
					++j;
			}
			else if (is_space((*argv)[j]))
				++j;
			else
				return (-1);
		}
		++argv;
	}
	return (count);
}
