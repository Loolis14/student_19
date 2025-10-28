/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:45:45 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:45:53 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h> //provides malloc and NULL
#include "libft.h" //provides ft_strlen

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

/*  #include <stdio.h>
int main()
{
	char s1[] = "shrek";
	char s2[] = " is real";
	printf("%s\n", ft_strjoin(s1, s2)); //shrek is real

	char s3[] = "shrek";
	char s4[] = "";
	printf("%s\n", ft_strjoin(s3, s4)); //shrek

	char s5[] = "";
	char s6[] = " is real";
	printf("%s\n", ft_strjoin(s5, s6)); // is real

	char s7[] = "";
	char s8[] = "";
	printf("%s\n", ft_strjoin(s7, s8)); //rien
} */