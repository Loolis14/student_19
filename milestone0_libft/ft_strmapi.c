/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:46:38 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 13:52:23 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h> //provides size_t
#include <stdlib.h> //provides malloc and NULL
#include "libft.h" //provides ft_strlen

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	size_t	i;
	char	*p;
	size_t	len_s;

	len_s = ft_strlen(s);
	p = malloc(len_s + 1);
	if (p == NULL)
	{
		return (NULL);
	}
	i = 0;
	while (s[i])
	{
		p[i] = f(i, s[i]);
		++i;
	}
	p[i] = '\0';
	return (p);
}

/* char	f_test(unsigned int i, char c)
{
	return (c + 1);
}

#include <stdio.h>
int main()
{
	char const s[] = "abcde";
	puts(ft_strmapi(s, f_test)); //bcdef
} */