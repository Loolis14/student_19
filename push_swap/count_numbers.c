//stack a = argv, stack b empty
#include "push_swap.h"
#include <unistd.h> //ssize_t

ssize_t 	count_numbers(char **argv)
{
	ssize_t	count;
	size_t	i;
	size_t	j;

	i = 0;
	count = 0;
	while(argv[i])
	{
		j = 0;
		while (argv[i][j])
		{
			if ((argv[i][j] == '+' || argv[i][j] == '-') && is_digit(argv[i][j + 1]))
			{
				++j;
				++count;
				while (is_digit(argv[i][j]))
				{
					++j;
				}
			}
			else if (is_digit(argv[i][j]))
			{
				++count;
				while (is_digit(argv[i][j]))
				{
					++j;
				}
			}
			else if (is_space(argv[i][j]))
			{
				++j;
			}
			else{
				return (-1);
			}
		}
		++i;
	}
	return (count);
}
