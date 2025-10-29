/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:45:36 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 13:24:53 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	size_t	i;

	i = 0;
	while (s[i])
	{
		f(i, &s[i]);
		++i;
	}
}

/* void	f_test(unsigned int i, char *c)
{
	c[i] = c[i] + 1;
}

#include <stdio.h>
int main()
{
	char s[] = "abcde"; //bcdef
	ft_striteri(s, f_test);
	puts(s);	
} */