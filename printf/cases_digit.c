/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cases_digit.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 23:07:46 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/29 23:07:50 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdarg.h> //provides va_
#include <unistd.h> //provides write and ssize_t

int	case_d(va_list args)
{
	char	*dec_base;
	ssize_t	count;
	int		n;

	dec_base = "0123456789";
	count = 0;
	n = va_arg(args, int);
	if (n < 0)
	{
		count += write(1, "-", 1);
	}
	count += ft_putnbr_base(ft_abs(n), dec_base);
	return (count);
}

int	case_i(va_list args)
{
	char	*dec_base;
	ssize_t	count;
	int		n;

	dec_base = "0123456789";
	count = 0;
	n = va_arg(args, int);
	if (n < 0)
	{
		count += write(1, "-", 1);
	}
	count += ft_putnbr_base(ft_abs(n), dec_base);
	return (count);
}

int	case_u(va_list args)
{
	char			*dec_base;
	ssize_t			count;
	unsigned int	n;

	dec_base = "0123456789";
	n = va_arg(args, unsigned int);
	count = ft_putnbr_base(n, dec_base);
	return (count);
}

int	case_x(va_list args)
{
	ssize_t				count;
	char				*hex_base;
	unsigned int		n;

	hex_base = "0123456789abcdef";
	n = va_arg(args, int);
	count = ft_putnbr_base(n, hex_base);
	return (count);
}

int	case_upper_x(va_list args)
{
	ssize_t				count;
	char				*hex_base;
	unsigned int		n;

	hex_base = "0123456789abcdef";
	n = va_arg(args, int);
	count = ft_putnbr_base(n, hex_base);
	return (count);
}
