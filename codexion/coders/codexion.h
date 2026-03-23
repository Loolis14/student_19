/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 21:23:47 by mmeurer           #+#    #+#             */
/*   Updated: 2026/03/23 16:40:21 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
# define CODEXION_H

#include <unistd.h>
#include <stdbool.h>

typedef enum logique {
	FIFO,
	EDF
} scheduler;

typedef struct ctx
{
	int				nb_coders;
	useconds_t		burnout;
	useconds_t		compile;
	useconds_t		debug;
	useconds_t		refactor;
	int				compiles_goal;
	useconds_t		dongle_cd;
	scheduler		scheduler;
}	ctx;

bool	main_parsing(char **args, ctx *context);

// utils
int		ft_len(char *s);

#endif //CODEXION_H