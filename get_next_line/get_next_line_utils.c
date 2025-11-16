/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 18:17:11 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/16 01:18:21 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	const unsigned char	*s2;

	s2 = s;
	c = (unsigned char) c;
	while (n)
	{
		if (*s2 == c)
		{
			return ((void *) s2);
		}
		++s2;
		--n;
	}
	return (NULL);
}

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t		i;
	char		*d;
	const char	*s;

	d = dest;
	s = src;
	i = 0;
	while (i != n)
	{
		d[i] = s[i];
		++i;
	}
	return (d);
}
