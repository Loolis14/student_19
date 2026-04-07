#include "codexion.h"

bool	init_mutex(t_ctx *ctx)
{
	if (pthread_mutex_init(ctx->stop_mutex, NULL) != 0)
	{
		return (false);
	}
	ctx->stop = false;
	if (pthread_mutex_init(ctx->print_mutex, NULL) != 0)
	{
		return (false);
	}
	return (true);
}

bool	create_monitor(&ctx)
{
	if (pthread_create(&ctx->monitor_thread, NULL, monitor_routine, &ctx) != 0)
	{
		return (false);
	}
	return (true);
}

bool    create_dongles(t_ctx *ctx)
{
    int i;

    i = 0;
    ctx->dongles = malloc(sizeof(t_dongle) * ctx->nb_coders);
    if (!ctx->dongles)
    {
        return (false);
    }
    while (i < ctx->nb_coders)
    {
        if (pthread_create(&ctx->dongles[i], NULL) != 0)
        {
            return (false);
        }
        if (pthread_mutex_init(&ctx->dongles[i].mutex, NULL) != 0)
        {
            return (false);
        }
        ctx->dongles[i].available = true;
            return (false);
        i++;
    }
    return (true);
}

bool    create_coders(t_ctx *ctx)
{
    int  i;

    ctx->coders = malloc(sizeof(t_coder) * ctx->nb_coders);
    if (!ctx->coders)
    {
        return (false);
    }
    i = 0;
    while (i < ctx->nb_coders)
    {
        ctx->coders[i].id = i + 1;
        ctx->coders[i].ctx = ctx;
        ctx->coders[i].last_compile = get_time();
        pthread_mutex_init(&ctx->coders[i].last_compile_mutex, NULL);

        if (pthread_create(&ctx->coders[i].thread, NULL, coroutine, &ctx->coders[i]) != 0)
        {
            return (false);
        }
        ++i;
    }
    return (true);
}

void join_threads(t_ctx *ctx)
{
    int i;

    i = 0;
    while (i < ctx->nb_coders)
    {
        pthread_join(ctx->coders[i].thread, NULL);
        i++;
    }
    pthread_join(ctx->monitor_thread, NULL);
}