/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cases_char.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 23:06:58 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/29 23:07:24 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h> //provides write and ssize_t
#include <stdint.h> //uintptr_t
#include <stdarg.h> //provides va_

int	case_c(va_list args)
{
	int		promoted;
	char	c;
	ssize_t	count;

	promoted = va_arg(args, int);
	c = promoted;
	count = write (1, &c, 1);
	return (count);
}

int	case_s(va_list args)
{
	char	*s;
	ssize_t	count;

	s = va_arg(args, char *);
	count = write (1, s, ft_strlen(s));
	return (count);
}

int	case_p(va_list args)
{
	char			*hex_base;
	uintptr_t		address;
	ssize_t			count;

	hex_base = "0123456789abcdef";
	count = 0;
	address = (uintptr_t)va_arg(args, void *);
	count += write (1, "0x", 2);
	count += ft_putnbr_base(address, hex_base);
	return (count);
}
