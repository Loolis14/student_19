#include "codexion.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	*collaborative_routine(void *arg)
{
    // c'est ici que je gere la routine de chaque philosopher. Mais du coup
    // ou mettre la gestion
	coder *coders = (coder *)arg;

/*     while (1)
	{
		eat(philo);
		sleep_philo(philo);
		think(philo);
	}
	return (NULL); */

    /*write(1, "coder ", 6);
    write(1, coders->id, strlen(coders->id));
    write(1, " est lancé\n", 12);*/

	printf("coder %d est lancé\n", coders->id);
	return (NULL);
}

bool create_thread()
{
    coder coders;

    coders.id = 1;
    pthread_create(&coders.thread, NULL, collaborative_routine, &coders);
    return (true);
}

bool create_threads(ctx *ctx)
{
    coder *coders;

    coders = malloc(sizeof(coder) * ctx->nb_coders);

    for (int i = 0; i < ctx->nb_coders; i++)
    {
        coders[i].id = i + 1;
        coders[i].ctx = ctx;

        pthread_create(&coders[i].thread, NULL, collaborative_routine, &coders[i]);
    }
    return (true);
}