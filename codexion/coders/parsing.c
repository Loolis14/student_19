/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 21:30:50 by mmeurer           #+#    #+#             */
/*   Updated: 2026/03/23 17:25:54 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// write,
//malloc, free,
// printf, fprintf, strcmp, strlen, atoi, memset

#include "codexion.h"
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>

bool	parse_int(char *s, int i, ctx *context)
{
	int	n;

	if (i == 0)
	{
		n = atoi(s);
		if (n < 1)
		{
			write(1, "First argument error: ", 22);
			write(1, "Number of coders not a positive integer.\n", 41);
			return false;
		}
		context->nb_coders = n;
	}
	else
	{
		n = atoi(s);
		if (n < 1)
		{
			write(1, "Sixth argument error: ", 22);
			write(1, "Number of compiles required not a positive integer.\n", 52);
			return false;
		}
		context->compiles_goal = n;
	}
	return (true);
}

bool	parse_usec(char *s, int i, ctx *context)
{
	int	n;
	bool	error = true;

	n = atoi(s);
	if (i == 1)
	{
		if (n < 1)
		{
			write(1, "Second argument error: ", 23);
			write(1, "Time to burnout not a positive integer.\n", 40);
			error = false;
		}
		context->burnout = (useconds_t) n;
	}
	else if (i == 2)
	{
		if (n < 1)
		{
			write(1, "Third argument error: ", 22);
			write(1, "Time to compile not a positive integer.\n", 40);
			error = false;
		}
		context->compile = (useconds_t) n;
	}
	else if (i == 3)
	{
		if (n < 1)
		{
			write(1, "Fourth argument error: ", 23);
			write(1, "Time to debug not a positive integer.\n", 38);
			error = false;
		}
		context->debug = (useconds_t) n;
	}
	else if (i == 4)
	{
		if (n < 1)
		{
			write(1, "Fifth argument error: ", 22);
			write(1, "Time to refactor not a positive integer.\n", 41);
			error = false;
		}
		context->refactor = (useconds_t) n;
	}
	else if (i == 6)
	{
		if (n < 1)
		{
			write(1, "Seventh argument error: ", 24);
			write(1, "Dongle cooldown not a positive integer.\n", 40);
			error = false;
		}
		context->dongle_cd = (useconds_t) n;
	}
	return error;
}

bool	parse_str(const char *s, ctx *context)
{
	const char	*fifo = "fifo";
	const char	*edf = "edf";

	if (strcmp(s, fifo) == 0)
	{
		context->scheduler = FIFO;
	}
	else if (strcmp(s, edf) == 0)
	{
		context->scheduler = EDF;
	}
	else
	{
		write(1, "Eighth argument error: ", 23);
		write(1, "Scheduler error. Usage: <fifo> or <edf>\n", 40);
		return (false);
	}
	return (true);
}


bool main_parsing(char **args, ctx *context)
{
	int i = 0;
	bool	error;

	error = true;
	while (i < 8)
	{
		if (i == 0 || i == 5)
		{
			if (!parse_int(args[i], i, context))
			{
				error = false;
			}
		}
		if (i == 7)
		{
			if (!parse_str(args[i], context))
			{
				error = false;
			}
		}
		else
		{
			if (!parse_usec(args[i], i, context))
			{
				error = false;
			}
		}
		++i;
	}
	return error;
}