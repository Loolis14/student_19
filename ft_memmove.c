/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:43:20 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:43:42 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	const char	*s;
	char		*d;

	s = src;
	d = dest;
	if (d <= s)
	{
		ft_memcpy(d, s, n);
	}
	else
	{
		s += n - 1;
		d += n - 1;
		while (n != 0)
		{
			*d-- = *s--;
			--n;
		}
	}
	return (dest);
}

/*#include <stdio.h>
int main()
{
	char str[50] = "Hello"; //d > s
	printf("%s\n", ft_memmove(str + 1,str, 5));

	char str2[50] = "Hello"; //d > s
	printf("%s\n", ft_memmove(str2 + 10,str2, 5));

	char str3[50] = "aaaaHello"; // d < s
	printf("%s\n", ft_memmove(str3,str3 + 4, 6));
} */