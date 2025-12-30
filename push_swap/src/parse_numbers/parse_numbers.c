/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_numbers.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:10:15 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/29 21:54:50 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_atoi(const char *nptr)
{
	unsigned int	nbr;
	int				neg;

	neg = 1;
	if (*nptr == '-' || *nptr == '+')
	{
		if (*nptr == '-')
		{
			neg = -1;
		}
		++nptr;
	}
	nbr = 0;
	while (*nptr >= '0' && *nptr <= '9')
	{
		nbr = nbr * 10 + (*nptr - '0');
		++nptr;
	}
	return (nbr * neg);
}

bool	parse_numbers(char **args, t_deque *a)
{
	size_t	i;
	size_t	j;
	int		number;

	i = 0;
	while (args[i])
	{
		j = 0;
		while (args[i][j])
		{
			if (is_space(args[i][j]))
			{
				++j;
			}
			else
			{
				number = ft_atoi(args[i] + j);
				//printf("%i", number);
				//vérifier > ou < a MIN int etc
				a->numbers[a->length] = number;
				++a->length;
				while (args[i][j] && !is_space(args[i][j]))
					++j;
			}
		}
		++i;
	}
	return (true);
}
