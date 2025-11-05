/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 16:59:39 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/05 22:45:13 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdlib.h> //provides malloc and NULL

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

char	*ft_strchr(const char *s, int c)
{
	c = (unsigned char) c;
	while (*s)
	{
		if (*s == c)
		{
			return ((char *) s);
		}
		++s;
	}
	if (c == '\0')
	{
		return ((char *) s);
	}
	return (NULL);
}

char	*ft_strdup(const char *s)
{
	char	*p;
	size_t	len_s;
	size_t	i;

	len_s = ft_strlen(s);
	p = malloc(len_s + 1);
	if (p == NULL)
	{
		return (NULL);
	}
	i = 0;
	while (s[i])
	{
		p[i] = s[i];
		++i;
	}
	p[i] = '\0';
	return (p);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*joined;
	char	*joined2;

	joined = malloc(ft_strlen(s1) + ft_strlen(s2) + 1);
	if (!joined)
	{
		return (NULL);
	}
	joined2 = joined;
	while (*s1)
	{
		*joined2 = *s1;
		++s1;
		++joined2;
	}
	while (*s2)
	{
		*joined2 = *s2;
		++s2;
		++joined2;
	}
	*joined2 = '\0';
	return (joined);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*p;
	char	*substr;
	size_t	i;

	if (!s)
		return (NULL);
	i = 0;
	while (i < start && s[i])
		++i;
	p = malloc(len + 1);
	if (!p)
		return (NULL);
	substr = p;
	while (len && s[i] != '\0')
	{
		*p = s[i];
		++i;
		--len;
		++p;
	}
	*p = '\0';
	return (substr);
}
