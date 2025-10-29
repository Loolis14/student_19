/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 23:08:28 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/29 23:08:31 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PRINTF_H
# define PRINTF_H
#include <stddef.h> //provides size_t
#include <stdarg.h> //provides va_list

int				ft_printf(const char *s, ...);
int				character_format(char s, va_list args);
size_t			ft_strlen(const char *str);
unsigned int	ft_abs(long long nbr);
int				ft_putnbr_base(long long nbr, char *base);

int				case_c(va_list args);
int				case_s(va_list args);
int				case_p(va_list args);
int				case_d(va_list args);
int				case_i(va_list args);
int				case_u(va_list args);
int				case_x(va_list args);
int				case_upper_x(va_list args);

#endif //PRINTF_H
