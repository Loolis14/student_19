/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 21:23:40 by mmeurer           #+#    #+#             */
/*   Updated: 2026/03/23 17:20:41 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"
#include <unistd.h>
#include <stdio.h>
#define USAGE "Usage: ./codexion <nbr_of_coders> <time_to_burnout> \
<time_to_compile> <time_to_debug> <time_to_refactor> \
<compilation_goal> <dongle_cooldown> <scheduler>\n"

int	main(int argc, char **argv)
{
	t_ctx	context;

	if (argc != 9)
	{
		printf("%s", "Bad number of arguments.\n" USAGE);
		return 1;
	}
	if (!main_parsing(argv + 1, &context))
	{
		return 1;
	}
	if (!init_mutex(&context))
	{
		return 1;
	}
	if (!create_dongles(&context) || !create_threads(&context))
	{
		return 1;
	}
	if (!create_monitor(&context))
	{
		return 1;
	}
	join_threads(&context); //Permet d'attendre que chaque thread est fini
	
	printf("%i\n", context.scheduler);
	printf("%i\n", context.nb_coders);
	printf("%u\n", context.burnout);
	printf("%u\n", context.compile);
	printf("%u\n", context.compiles_goal);
}