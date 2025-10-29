/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:47:12 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:47:24 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h> //provides size_t
#include <stdlib.h> //provides malloc and NULL
#include "libft.h" //provides ft_strlen and ft_strdup

static int	is_sep(char const *s1, char const *set)
{
	size_t	i;

	while (*s1)
	{
		i = 0;
		while (*set)
		{
			if (set[i] == *s1)
			{
				return (1);
			}
			++set;
		}
		++s1;
	}
	return (0);
}

size_t	ft_len_expected(char const *s1, char const *start, char const *set)
{
	size_t		len_expected;

	len_expected = ft_strlen(start);
	s1 += len_expected;
	if (is_sep(s1 - 1, set) == 1)
	{
		--s1;
		--len_expected;
		while ((s1 > start) && is_sep(s1 - 1, set) == 1)
		{
			--s1;
			--len_expected;
		}
	}
	return (len_expected);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	char		*trimed;
	char		*trimed2;
	char const	*start;
	size_t		len_expected;

	while (is_sep(s1, set) == 1)
		++s1;
	start = s1;
	if (*start == '\0')
	{
		return (ft_strdup(""));
	}
	len_expected = ft_len_expected(s1, start, set);
	trimed = malloc(len_expected + 1);
	if (!trimed)
		return (NULL);
	trimed2 = trimed;
	while (len_expected)
	{
		*trimed++ = *start++;
		--len_expected;
	}
	*trimed = '\0';
	return (trimed2);
}

/* #include <stdio.h>
int main ()
{
	char const s1[] = "aaaa"; //(vide)
	char const set1[] = "a";
	printf("%s\n", ft_strtrim(s1, set1));

	char const s2[] = " je suis ici    "; //je suis ici
	char const set2[] = " ";
	printf("%s\n", ft_strtrim(s2, set2));

	char const s3[] = "**--shrek*-"; //shrek*-
	char const set3[] = "*";
	printf("%s\n", ft_strtrim(s3, set3));

	char const s4[] = ""; //(vide)
	char const set4[] = "+";
	printf("%s\n", ft_strtrim(s4, set4));

	char const s5[] = "shrek"; //(shrek)
	char const set5[] = "";
	printf("%s\n", ft_strtrim(s5, set5));
} */