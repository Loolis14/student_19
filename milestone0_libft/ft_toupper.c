/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:47:47 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:47:56 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_toupper(int c)
{
	if (c >= 'a' && c <= 'z')
	{
		return (c ^ 32);
	}
	return (c);
}

/*  #include <stdio.h>
int main()
{
    int c = 'g';
    printf("%c\n", ft_toupper(c)); //G

	int t = '-';
    printf("%c\n", ft_toupper(t)); //-
} */