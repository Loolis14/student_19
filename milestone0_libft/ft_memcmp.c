/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:43:10 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:43:10 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	const char	*s1_2;
	const char	*s2_2;

	s1_2 = s1;
	s2_2 = s2;
	if (n == 0)
	{
		return (0);
	}
	while ((*s1_2 == *s2_2) && --n != 0)
	{
		++s1_2;
		++s2_2;
	}
	return ((unsigned char)*s1_2 - (unsigned char)*s2_2);
}

/* #include <stdio.h>
int main()
{
	const char s1 [] = "ABC";
	const char s2 [] = "ABC";
	printf("%i\n", ft_memcmp(s1,s2,3)); //0

	const char a1 [] = "ABC";
	const char a2 [] = "AB";
	printf("%i\n", ft_memcmp(a1,a2,3)); //67

	const char d1 [] = "AB";
	const char d2 [] = "ABC";
	printf("%i\n", ft_memcmp(d1,d2,3)); //-67

	const char b1 [] = "ABA";
	const char b2 [] = "ABZ";
	printf("%i\n", ft_memcmp(b1,b2,3)); //-25

	const char c1 [] = "ABA";
	const char c2 [] = "ABZ";
	printf("%i\n", ft_memcmp(c1,c2,0)); //0
} */