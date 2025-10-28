/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:47:41 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:47:42 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_tolower(int c)
{
	if (c >= 'A' && c <= 'Z')
	{
		return (c ^ 32);
	}
	return (c);
}

/* 
#include <stdio.h>
int main()
{
	int c = 'G';
	printf("%c\n", ft_tolower(c)); //g

	int a = '*';
	printf("%c\n", ft_tolower(a)); //\*
} */