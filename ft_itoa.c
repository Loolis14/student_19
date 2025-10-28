/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:37:30 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:37:32 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h> //provides len_t
#include <stdlib.h> //provides malloc and NULL
#include <stdio.h>

static size_t	len_number(unsigned int n)
{
	size_t	i;

	i = 0;
	while (n >= 10)
	{
		n = n / 10;
		++i;
	}
	++i;
	return (i);
}

static unsigned int	ft_abs(int n)
{
	if (n < 0)
	{
		return (-(unsigned)n);
	}
	return (n);
}

static char	*ft_malloc(size_t len_n, size_t neg)
{
	char			*p;

	p = malloc(sizeof(char) * (len_n + 1 + neg));
	if (p == NULL)
	{
		return (NULL);
	}
	return (p);
}

char	*ft_itoa(int n)
{
	char			*p;
	size_t			neg;
	size_t			len_n;
	unsigned int	n2;

	neg = n < 0;
	n2 = ft_abs(n);
	len_n = len_number(n2);
	p = ft_malloc(len_n, neg);
	p += len_n + neg;
	*p = '\0';
	while (n2 >= 10)
	{
		*--p = n2 % 10 + '0';
		n2 = n2 / 10;
	}
	*--p = n2 % 10 + '0';
	if (neg == 1)
	{
		*--p = '-';
	}
	return (p);
}

/* #include <stdio.h>
int	main()
{
	printf("%s\n", ft_itoa(10));
	printf("%s\n", ft_itoa(-513));
	printf("%s\n", ft_itoa(2387));
} */