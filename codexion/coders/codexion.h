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
#include <pthread.h>

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

typedef struct coder {
	int			id;
	pthread_t	thread;
	useconds_t	last_compile;
	int			nb_code;
	ctx			*ctx;
} coder;

bool	main_parsing(char **args, ctx *context);
bool create_threads(ctx *ctx);

// utils
int		ft_len(char *s);

#endif //CODEXION_H