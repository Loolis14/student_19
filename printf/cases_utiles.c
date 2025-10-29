/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cases_utiles.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 22:58:40 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/29 23:06:25 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stddef.h> //provides size_t
#include <unistd.h> //provides write and ssize_t

size_t	ft_strlen(const char *str)
{
	size_t	len;

	len = 0;
	while (str[len])
	{
		++len;
	}
	return (len);
}

unsigned int	ft_abs(long long nbr)
{
	if (nbr < 0)
	{
		return (-(unsigned int)nbr);
	}
	return (nbr);
}

int	ft_putnbr_base(long long nbr, char *base)
{
	char				c;
	ssize_t				count;
	long long			size;

	count = 0;
	size = ft_strlen(base);
	if (nbr >= size)
	{
		count += ft_putnbr_base(((long long) nbr / size), base);
	}
	c = base[nbr % size];
	count += write (1, &c, 1);
	return (count);
}
