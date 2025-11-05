/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 10:34:44 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/05 13:39:27 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

ssize_t	character_format(char s, va_list args)
{
	ssize_t	count;

	if (s == 'c')
		count = case_c(args);
	else if (s == 's')
		count = case_s(args);
	else if (s == 'p')
		count = case_p(args);
	else if (s == 'd')
		count = case_d(args);
	else if (s == 'i')
		count = case_i(args);
	else if (s == 'u')
		count = case_u(args);
	else if (s == 'x')
		count = case_x(args);
	else if (s == 'X')
		count = case_upper_x(args);
	else if (s == '%')
		count = write(STDOUT_FILENO, "%", 1);
	return (count);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	size_t	i;
	ssize_t	count;	

	va_start(args, format);
	i = 0;
	count = 0;
	while (format[i])
	{
		if (format[i] == '%' && is_supported(format[i + 1]))
		{
			count += character_format(format[i + 1], args);
			i += 2;
		}
		else
		{
			count += write(STDOUT_FILENO, &format[i], 1);
			++i;
		}
	}
	va_end(args);
	return (count);
}

#include <stdio.h>
int main()
{
	//one of each
	char s[] = "Le %% de chance es%c de %d ou %i ou %u, en hexadecimal %x ou %X";
	printf(" %i\n", ft_printf(s, 't', 10, 50, 70, 80, 100));
	printf(" %i\n", printf(s, 't', 10, 50, 70, 80, 100));

	//pointeur
	char s2[] = "l'adresse du %s s2 est %p";
	printf(" %i\n", ft_printf(s2, "pointeur", s2));
	printf(" %i\n", printf(s2,"pointeur", s2));

	//particulary cases
	char s3[] = "Si un string est vide : %s, et pour les nombres négatifs : \
	%d, %i, (unsigned) %u, (hexadécimal) %x, %X";
	printf(" %i\n", ft_printf(s3, "", -2, -56, -46874, -795322, 0));
	printf(" %i\n", printf(s3,"", -2, -56, -46874, -795322, 0));

	{
	char s3[] = "Si un format n'est pas reconnu : %Q ";
	printf(" %i\n", ft_printf(s3, ""));
	printf(" %i\n", printf(s3,""));
	}
}