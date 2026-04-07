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
} t_scheduler;

typedef struct t_ctx ctx;

typedef struct s_coder {
	int				id;
	pthread_t		thread;
	useconds_t		last_compile;
	pthread_mutex_t last_compile_mutex;
	int				nb_code;
	t_ctx			*ctx;
	t_dongle 		*left_dongle;
	t_dongle 		*right_dongle;
} 	t_coder;

typedef struct s_ctx {
	int				nb_coders;
	useconds_t		burnout;
	useconds_t		compile;
	useconds_t		debug;
	useconds_t		refactor;
	int				compiles_goal;
	useconds_t		dongle_cd;
	t_scheduler		scheduler;

	t_coder			*coders;
	pthread_t 		monitor_thread;
	bool       		stop;
	t_dongle		*dongles;
	pthread_mutex_t stop_mutex;
	pthread_mutex_t print_mutex;
}	t_ctx;

typedef struct s_dongle {
    pthread_mutex_t mutex;
    pthread_cond_t  cond;

    bool             available;
    
    // file d'attente
    // (FIFO ou priority queue pour EDF)

} t_dongle;

bool	main_parsing(char **args, t_ctx *context);

//initialisation
bool	init_mutex(t_ctx *ctx);
bool	create_monitor(&ctx);
bool 	create_coders(t_ctx *ctx);
bool    create_dongles(t_ctx *ctx)
void 	join_threads(t_ctx *ctx);


// utils
int		ft_len(char *s);

#endif //CODEXION_H