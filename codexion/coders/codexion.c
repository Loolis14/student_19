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
	ctx	contexte;
	if (argc != 9)
	{
		printf("%s", "Bad number of arguments.\n" USAGE);
		return 1;
	}
	if (!main_parsing(argv + 1, &contexte))
	{
		return 1;
	}
	if (!create_dongles(&contexte))
	{
		return 1;
	}
	if (!create_threads(&contexte))
	{
		return 1;
	}
	join_threads(&contexte); //Permet d'attendre que chaque thread est fini
	printf("%i\n", contexte.scheduler);
	printf("%i\n", contexte.nb_coders);
	printf("%u\n", contexte.burnout);
	printf("%u\n", contexte.compile);
	printf("%u\n", contexte.compiles_goal);
}