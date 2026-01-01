/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_numbers.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:10:15 by mmeurer           #+#    #+#             */
/*   Updated: 2026/01/01 23:32:24 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <limits.h>

bool	check_overflow(unsigned int nbr, unsigned int n, int sign)
{
	unsigned int	other_digits;
	unsigned int	last_digit;

	if (sign == 1)
	{
		other_digits = INT_MAX / 10;
		last_digit = INT_MAX % 10;
	}
	else
	{
		other_digits = ((unsigned int)INT_MAX + 1) / 10;
		last_digit = ((unsigned int)INT_MAX + 1) % 10;
	}
	if (nbr > other_digits || (nbr == other_digits && n > last_digit))
		return (false);
	return (true);
}

static bool	ft_atoi(const char *nptr, int *number)
{
	unsigned int	nbr;
	int				sign;

	sign = 1;
	if (*nptr == '-' || *nptr == '+')
	{
		if (*nptr == '-')
		{
			sign = -1;
		}
		++nptr;
	}
	nbr = 0;
	while (*nptr >= '0' && *nptr <= '9')
	{
		if (!check_overflow(nbr, *nptr - '0', sign))
		{
			return (false);
		}
		nbr = nbr * 10 + (*nptr - '0');
		++nptr;
	}
	*number = nbr * sign;
	return (true);
}

bool	parse_numbers(char **args, t_deque *a)
{
	size_t	j;
	int		number;

	while (*args)
	{
		j = 0;
		while ((*args)[j])
		{
			if (is_space((*args)[j]))
				++j;
			else
			{
				if (!ft_atoi(*args + j, &number))
					return (false);
				a->numbers[a->length] = number;
				++a->length;
				while ((*args)[j] && !is_space((*args)[j]))
					++j;
			}
		}
		++args;
	}
	return (true);
}
