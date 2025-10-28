/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:47:29 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 14:14:56 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides ft_strlen
#include <stddef.h> //provides size_t
#include <stdlib.h> //provides malloc and NULL

static size_t	min(size_t len, size_t i)
{
	if (len < i)
	{
		return (len);
	}
	return (i);
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
	p = malloc(min(len, ft_strlen(&s[i])) + 1);
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

/* #include <stdio.h>
int	main()
{
	char s[] = "shrek is real"; //is real
	printf("%s\n", ft_substr(s, 6, 7));
} */