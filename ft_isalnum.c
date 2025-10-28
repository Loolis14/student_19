/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:36:43 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:36:49 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_isalnum(int c)
{
	if (c >= '0' && c <= '9')
	{
		return (1);
	}
	if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
	{
		return (1);
	}
	return (0);
}

/*  #include <stdio.h>

int	main ()
{
	char	c = 'i';
	printf("%d\n",ft_isalnum(c)); //0
	char	d = 'D';
	printf("%d\n",ft_isalnum(d)); //1
	char e = '3';
	printf("%d\n",ft_isalnum(e)); //1
	char f = '*';
	printf("%d\n",ft_isalnum(f)); //0
} */