#include "codexion.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool    simulation_stop(t_ctx *ctx)
{
    bool    stop;

    pthread_mutex_lock(&ctx->stop_mutex);
    stop = ctx->stop;
    pthread_mutex_unlock(&ctx->stop_mutex);

    return (stop);
}

void take_dongle(t_dongle *d)
{
    pthread_mutex_lock(&d->mutex);

    while (d->available == 0)
    {
        pthread_cond_wait(&d->cond, &d->mutex);
    }

    d->available = 0;

    pthread_mutex_unlock(&d->mutex);
}

void	*coroutine(void *arg)
{
	t_coder *c = (t_coder *)arg;

    while (!simulation_stop(c->ctx)) //check les conditions de stop
	{
		pthread_mutex_lock(&c->last_compile_mutex);
        c->last_compile = get_time();
        pthread_mutex_unlock(&c->last_compile_mutex);
        //compile(c);
		//debug(c);
		//refactor(c);
	}

    pthread_mutex_lock(&ctx->print_mutex);
	printf("coder %d est lancé\n", c->id);
    pthread_mutex_unlock(&ctx->print_mutex);

	return (NULL);
}

void *monitor_routine(void *arg)
{
    t_ctx *ctx = (t_ctx *)arg;
    int i;

    while (1)
    {
        i = 0;
        while (i < ctx->nb_coders)
        {
            pthread_mutex_lock(&ctx->coders[i].last_compile_mutex);

            if (get_time() - ctx->coders[i].last_compile > ctx->burnout)
            {
                pthread_mutex_unlock(&ctx->coders[i].last_compile_mutex);

                pthread_mutex_lock(&ctx->stop_mutex);
                ctx->stop = 1;
                pthread_mutex_unlock(&ctx->stop_mutex);
                
                pthread_mutex_lock(&ctx->print_mutex);
                printf("coder %d est mort 💀\n", ctx->coders[i].id);
                pthread_mutex_unlock(&ctx->print_mutex);
                return (NULL);
            }

            pthread_mutex_unlock(&ctx->coders[i].last_compile_mutex);
            i++;
        }
        usleep(1000);
    }
}
