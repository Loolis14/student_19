/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cases_utils.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 22:58:40 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/02 21:20:53 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h>

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

unsigned int	ft_abs(int nbr)
{
	if (nbr < 0)
	{
		return (-(unsigned int)nbr);
	}
	return (nbr);
}

ssize_t	ft_putnbr_base(uintmax_t nbr, char *base)
{
	char	c;
	ssize_t	count;
	size_t	size;

	count = 0;
	size = ft_strlen(base);
	if (nbr >= size)
	{
		count += ft_putnbr_base(((uintmax_t) nbr / size), base);
	}
	c = base[nbr % size];
	count += write(STDOUT_FILENO, &c, 1);
	return (count);
}

bool	is_supported(char c)
{
	const char *s;

	s = "cspdiuxX%";
	while (*s)
	{
		if (*s == c)
		{
			return (true);
		}
		++s;
	}
	return (false);
}
