#include "codexion.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



void	*coroutine(void *arg)
{
    // c'est ici que je gere la routine de chaque philosopher. Mais du coup
    // ou mettre la gestion ?
	coder *c = (coder *)arg;

    while (!simulation_stop(c->ctx)) //check les conditions de stop
	{
		//compile(c);
		//debug(c);
		//refactor(c);
	}

	printf("coder %d est lancé\n", c->id);
	return (NULL);
}

void join_threads(ctx *ctx)
{
    int i;

    i = 0;
    while (i < ctx->nb_coders)
    {
        pthread_join(ctx->coders[i].thread, NULL);
        i++;
    }
}

bool    create_dongles(ctx *ctx)
{
    int i;

    i = 0;
    ctx->forks = malloc(sizeof(pthread_mutex_t) * ctx->nb_coders);
    if (!ctx->forks)
    {
        return (false);
    }
    while (i < ctx->nb_coders)
    {
        if (pthread_mutex_init(&ctx->forks[i], NULL) != 0)
            return (false);
        i++;
    }
    return (true);
}

bool    create_coders(ctx *ctx)
{
    int  i;

    ctx->coders = malloc(sizeof(coder) * ctx->nb_coders);
    if (!ctx->coders)
    {
        return (false);
    }
    i = 0;
    while (i < ctx->nb_coders)
    {
        ctx->coders[i].id = i + 1;
        ctx->coders[i].ctx = ctx;

        if (pthread_create(&ctx->coders[i].thread, NULL, coroutine, &ctx->coders[i]) != 0)
        {
            return (false);
        }
        ++i;
    }
    return (true);
}