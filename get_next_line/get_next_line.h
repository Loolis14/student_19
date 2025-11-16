/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 18:17:06 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/16 01:20:39 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <stddef.h> //provides size_t

typedef struct s_buffer
{
	char	*content;
	size_t	capacity;
	size_t	length;
}	t_buffer;

char	*get_next_line(int fd);

void	*ft_memchr(const void *s, int c, size_t n);
void	*ft_memcpy(void *dest, const void *src, size_t n);

#endif //GET_NEXT_LINE_H