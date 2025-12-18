#include "push_swap.h"
#include <stddef.h>
#include <unistd.h>
#include <stdlib.h>

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

int	*parse_numbers(char **args, ssize_t count)
{
	int	*numbers;
	size_t	i;
	size_t	j;
	size_t	k;
	int	number;

	numbers = malloc(sizeof(int) * count);
	if (numbers == NULL)
	{
		return (NULL);
	}
	i = 0;
	k = 0;
	while (args[i])
	{
		j = 0;
		while (args[i][j])
		{
			if (is_space(args[i][j]))
			{
				++j;
			}
			else {
				number = ft_atoi(args[i] + j);
				//printf("%i", number);
				//vérifier > ou < a MIN int etc
				numbers[k] = number;
				++k;
			}
			while (args[i][j] && !is_space(args[i][j]))
				++j;
		}
		++i;
	}
	return (numbers);
}