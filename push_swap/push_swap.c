/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 17:39:20 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/18 17:50:29 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stddef.h>
#include <stdio.h> //ssize_t

int main(int argc, char **argv)
{
	int	*numbers;
	ssize_t count;
	size_t i= 0;
	
	if (argc == 1 || (ft_strncmp(argv[1], "", 1) == 0))
	{
		return (0);
	}
	count = count_numbers(argv + 1);
	if (count == -1 || count == 0)
	{
		printf("%s", "Error\n");
		return (0);
	}
	numbers = parse_numbers(argv + 1, count);
	if (numbers == NULL)
	{
		printf("%s", "Error\n");
		return (0);
	}


	//print les nombres
	/* while (i < 4)
	{
		printf("%i\n", numbers[i]);
		++i;
	} */
}