/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:46:52 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:46:52 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include "libft.h" // provides ft_strlen et ft_strncmp

char	*ft_strnstr(const char *haystack, const char *needle, size_t n)
{
	size_t	i;
	size_t	len_needle;

	i = 0;
	if (needle[0] == '\0')
	{
		return ((char *) haystack);
	}
	len_needle = ft_strlen(needle);
	while (haystack[i] && i + len_needle <= n)
	{
		if (ft_strncmp(&haystack[i], needle, len_needle) == 0)
		{
			return ((char *) &haystack[i]);
		}
		++i;
	}
	return (NULL);
}

/* #include <stdio.h>
int main()
{
	const char s[] = "shrek"; //rek
	const char d[] = "re";
	printf("%s", ft_strnstr(s,d,10)); 
	printf("\n");

	const char s2[] = "shrekre"; //rekre
	const char d2[] = "re";
	printf("%s\n", ft_strnstr(s2, d2, 7));

	const char s1[] = "shrek"; //shrek
	const char d1[] = "";
	char *s12 = ft_strnstr(s1, d1, 5);
	if (s12 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s12);
	}

	const char s3[] = "shrek"; //NULL
	const char d3[] = "i";
	char *s22 = ft_strnstr(s3, d3, 20);
	if (s22 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s22);
	}

	const char s4[] = "shrek"; //NULL
	const char d4[] = "re";
	char *s32 = ft_strnstr(s4, d4, 0);
	if (s32 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s32);
	}
} */