/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:46:57 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 12:28:34 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

char	*ft_strrchr(const char *s, int c)
{
	const char	*temp;

	c = (unsigned char) c;
	temp = NULL;
	while (*s)
	{
		if (*s == c)
		{
			temp = s;
		}
		++s;
	}
	if (c == '\0')
	{
		return ((char *)s);
	}
	return ((char *)temp);
}

/* #include <stdio.h>
int main()

{
	const char s[] = "shrekhop"; //hop
	printf("%s\n", ft_strrchr(s, 'h'));

	const char s1[] = "shrek"; //NULL
	char *s12 = ft_strrchr(s1, 'i');
	if (s12 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s12);
	}

	const char s3[] = "shrek"; //(vide)
	char *s32 = ft_strrchr(s3, '\0');
	if (s32 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s32);
	}

	const char s4[] = "shrekrek"; //ek
	printf("%s\n", ft_strrchr(s4, 'e'));
} */