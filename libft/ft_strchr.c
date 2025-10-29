/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:45:25 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 12:28:39 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

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


/*  #include <stdio.h>
int main()

{
	const char s[] = "shrek"; //hrek
	printf("%s\n", ft_strchr(s, 'h'));

	const char s1[] = "shrek"; //NULL
	char *s12 = ft_strchr(s1, 'i');
	if (s12 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s12);
	}

	const char s3[] = "shrek"; //(vide)
	char *s32 = ft_strchr(s3, '\0');
	if (s32 == NULL)
	{
		puts("null");
	}
	else {
	printf("%s\n", s32);
	}

	const char s4[] = "shrekrek"; //ekrek
	printf("%s\n", ft_strchr(s4, 'e'));
}
 */