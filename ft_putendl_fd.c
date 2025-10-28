/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:44:07 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:44:08 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h> //provides write
#include "libft.h" //provides ft_strlen

void	ft_putendl_fd(char *s, int fd)
{
	write (fd, s, ft_strlen(s));
	write (fd, "\n", 1);
}

/* int main()
{
	ft_putendl_fd("shrek", 1);
} */