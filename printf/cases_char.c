/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cases_char.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 23:06:58 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/05 13:34:02 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

ssize_t	case_c(va_list args)
{
	int				promoted;
	unsigned char	c;

	promoted = va_arg(args, int);
	c = promoted;
	return (write(STDOUT_FILENO, &c, 1));
}

ssize_t	case_s(va_list args)
{
	char	*s;

	s = va_arg(args, char *);
	return (write(STDOUT_FILENO, s, ft_strlen(s)));
}

ssize_t	case_p(va_list args)
{
	char			*hex_base;
	uintptr_t		address;
	ssize_t			count;

	hex_base = "0123456789abcdef";
	count = 0;
	address = (uintptr_t)va_arg(args, void *);
	count += write(STDOUT_FILENO, "0x", 2);
	count += ft_putnbr_base(address, hex_base);
	return (count);
}
