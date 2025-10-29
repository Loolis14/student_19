/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:43:15 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:43:17 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t		i;
	char		*d;
	const char	*s;

	d = dest;
	s = src;
	i = 0;
	while (i != n)
	{
		d[i] = s[i];
		++i;
	}
	return (d);
}

/* #include <stdio.h>
int main()
{
	char s[] = "shrek76";
	char d[sizeof s] = {[sizeof s - 1] = 0};
	printf("%s\n",ft_memcpy(d, s, 7));
} */