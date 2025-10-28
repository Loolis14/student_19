/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:43:55 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:43:56 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

void	*ft_memset(void *s, int c, size_t n)
{
	char	*s2;

	s2 = s;
	while (n > 0)
	{
		*s2 = c;
		++s2;
		--n;
	}
	return (s);
}

/*  #include <stdio.h>

int main()
{
	char buffer[10] = {0};
	ft_memset(buffer, 'c', 2);
	puts(buffer); //cc
} */