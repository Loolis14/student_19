/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 21:23:40 by mmeurer           #+#    #+#             */
/*   Updated: 2026/03/19 22:04:59 by mmeurer          ###   ########.fr       */
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
	if (argc != 9)
	{
		printf("%s", "Bad number of arguments.\n" USAGE);
		return 1;
	}
	main_parsing(argv + 1);
}