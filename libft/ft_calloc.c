/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:36:17 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:36:17 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h> //provides malloc and NULL
#include "libft.h" //provides ft_bzero
#include <stdint.h> //provides SIZE_MAX

void	*ft_calloc(size_t nmemb, size_t size)
{
	char	*p;

	if (size != 0 && nmemb > SIZE_MAX / size)
	{
		return (NULL);
	}
	if (nmemb == 0 || size == 0)
	{
		nmemb = 1;
		size = 1;
	}
	p = malloc(nmemb * size);
	if (p == NULL)
	{
		return (NULL);
	}
	ft_bzero(p, nmemb * size);
	return (p);
}
