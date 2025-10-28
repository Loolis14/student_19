/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:34:44 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:34:44 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdbool.h>

int	ft_atoi(const char *nptr)
{
	unsigned int	nbr;
	bool			is_negative;

	nbr = 0;
	while (*nptr == ' ' || (*nptr >= '\t' && *nptr <= '\r'))
	{
		++nptr;
	}
	is_negative = *nptr == '-';
	if (is_negative || *nptr == '+')
	{
		++nptr;
	}
	while (*nptr >= '0' && *nptr <= '9')
	{
		nbr = nbr * 10 + *nptr - '0';
		++nptr;
	}
	if (is_negative)
	{
		return (-nbr);
	}
	return (nbr);
}

/* #include <stdlib.h>
#include <stdio.h>

int main()
{
	const char *s1 = "-123"; //-123
	printf("%i\n",atoi(s1));
	printf("%i\n",ft_atoi(s1));

	const char *s2 = "      123+2"; //123
	printf("%i\n",atoi(s2));
	printf("%i\n",ft_atoi(s2));

	const char *s3 = "-+123a"; //-123
	printf("%i\n",atoi(s3));
	printf("%i\n",ft_atoi(s3));

	const char *s4 = "+123a"; //123
	printf("%i\n",atoi(s4));
	printf("%i\n",ft_atoi(s4));

	const char *s5 = "+a123a"; //0
	printf("%i\n",atoi(s5));
	printf("%i\n",ft_atoi(s5));

	const char *s6 = "-azih123"; //0
	printf("%i\n",atoi(s6));
	printf("%i\n",ft_atoi(s6));      
} */