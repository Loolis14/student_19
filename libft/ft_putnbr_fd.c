/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:44:14 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:44:34 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h> //provides write

static unsigned int	ft_abs(int n)
{
	if (n < 0)
	{
		return (-(unsigned)n);
	}
	return (n);
}

void	ft_putnbr_fd(int n, int fd)
{
	unsigned int	nb;
	unsigned int	c;

	if (n < 0)
	{
		write (fd, "-", 1);
	}
	nb = ft_abs(n);
	if (nb >= 10)
	{
		ft_putnbr_fd(nb / 10, fd);
	}
	c = nb % 10 + '0';
	write (fd, &c, 1);
}

/* int main()
{
    ft_putnbr_fd(10, 1);
    write (1, "\n", 1);
    ft_putnbr_fd(-10, 1);
    write (1, "\n", 1);
    ft_putnbr_fd(0, 1);
    write (1, "\n", 1);
} */