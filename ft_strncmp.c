/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:46:46 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:46:48 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h> //provides size_t

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	if (n == 0)
	{
		return (0);
	}
	while (*s1 == *s2 && --n != 0)
	{
		++s1;
		++s2;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

/* #include <stdio.h>
int main()
{
	const char s1 [] = "ABC";
	const char s2 [] = "ABC";
	printf("%i\n", ft_strncmp(s1,s2,3)); //0

	const char a1 [] = "ABC";
	const char a2 [] = "AB";
	printf("%i\n", ft_strncmp(a1,a2,3)); //67

	const char d1 [] = "AB";
	const char d2 [] = "ABC";
	printf("%i\n", ft_memcmp(d1,d2,3)); //-67

	const char b1 [] = "ABA";
	const char b2 [] = "ABZ";
	printf("%i\n", ft_strncmp(b1,b2,1)); //0
}*/