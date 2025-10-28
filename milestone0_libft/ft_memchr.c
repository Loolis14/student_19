/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:42:49 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:42:49 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h> //provides NULL

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

/* int main()

{
	const char s[] = "shrek"; //hrek
	printf("%s\n", (char*)ft_memchr(s, 'h', 5));

	const char s1[] = "shrek"; //NULL
	char *s12 = ft_memchr(s1, 'i', 5);
	if (s12 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s12);
	}

	const char s2[] = "shrek"; //NULL
	char *s22 = ft_memchr(s2, 'i', 0);
	if (s22 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s22);
	}

	const char s3[] = "shrek"; //NULL
	char *s32 = ft_memchr(s3, '\0', 5);
	if (s32 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s32);
	}

	const char s4[] = "shrekrek"; //ekrek
	printf("%s\n", (char*)ft_memchr(s4, 'e', 8));
}
 */