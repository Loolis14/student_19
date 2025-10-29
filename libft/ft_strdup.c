/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:45:30 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 11:03:30 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h> //provides size_t
#include <stdlib.h> //provides malloc and NULL
#include "libft.h" //provide ft_strlen and ft_strlcpy

char	*ft_strdup(const char *s)
{
	char	*p;
	size_t	len_s;

	len_s = ft_strlen(s);
	p = malloc(len_s + 1);
	if (p == NULL)
	{
		return (NULL);
	}
	ft_strlcpy(p, s, len_s + 1);
	return (p);
}

/* #include <stdio.h>
int	main()
{
	char s[] = "shrek+";
	printf("%s", ft_strdup(s));
} */