/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:44:40 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:44:41 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h> //provides write
#include "libft.h" //provides ft_strlen

void	ft_putstr_fd(char *s, int fd)
{
	write (fd, s, ft_strlen(s));
}

/* int main()
{
	ft_putstr_fd("shrek", 1);
} */