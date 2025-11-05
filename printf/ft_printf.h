/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 23:08:28 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/05 13:37:33 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include <stddef.h> //provides size_t
# include <stdarg.h> //provides va_list
# include <stdint.h>
# include <unistd.h> //provides ssize_t and write
# include <stdbool.h>

int				ft_printf(const char *s, ...);
ssize_t			character_format(char s, va_list args);
size_t			ft_strlen(const char *str);
unsigned int	ft_abs(int nbr);
ssize_t			ft_putnbr_base(uintmax_t nbr, char *base);
bool			is_supported(char c);

ssize_t			case_c(va_list args);
ssize_t			case_s(va_list args);
ssize_t			case_p(va_list args);
ssize_t			case_d(va_list args);
ssize_t			case_i(va_list args);
ssize_t			case_u(va_list args);
ssize_t			case_x(va_list args);
ssize_t			case_upper_x(va_list args);

#endif //FT_PRINTF_H
