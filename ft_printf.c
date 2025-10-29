/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 10:34:44 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/29 23:08:23 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdarg.h> //provides va
#include <stddef.h> //provides size_t
#include <unistd.h> //provides write and ssize_t

int	character_format(char s, va_list args)
{
	size_t	count;

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
		count = write (1, "%", 1);
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
		if (format[i] == '%')
		{
			count += character_format(format[i + 1], args);
			i += 2;
		}
		else
		{
			count += write (1, &format[i], 1);
			++i;
		}
	}
	va_end(args);
	return (count);
}

/* #include <stdio.h>
int main()
{
	char s[] = "printf est égal %% il est %d";
	//char s2[] = "printf est %s";
	//char p[] = "shrek";
	//ft_printf(s, 14, "shrek");
	//printf("%p\n", 14);
	printf(" %i\n", ft_printf(s, 2));
	printf(" %i\n", printf(s, 2));
} */