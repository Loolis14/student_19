/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:46:03 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:46:03 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t sz)
{
	size_t	i;
	size_t	len_dst;
	size_t	len_src;

	i = 0;
	len_dst = ft_strlen(dst);
	len_src = ft_strlen(src);
	if (sz <= len_dst)
		return (sz + len_src);
	while (dst[i])
		++i;
	while (i < sz - 1 && *src)
	{
		dst[i] = *src;
		++i;
		++src;
	}
	dst[i] = '\0';
	return (len_dst + len_src);
}

/* #include <stdio.h> 
int main()
{
	char d[20] = "hello"; 
	char s[] = "world";
	printf("%zi\n",ft_strlcat(d,s,8));//10
	puts(d);//hellowo
	char d1[] = "hello"; 
	char s1[] = "world";
	printf("%zi\n",ft_strlcat(d1,s1,5)); //10
	puts(d1); //hello
	char d2[] = "hi"; 
	char s2[] = "shrek";
	printf("%zi\n",ft_strlcat(d2,s2,1)); //6
	puts(d2); //hi
} */