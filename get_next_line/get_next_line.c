/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 18:17:18 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/16 01:23:49 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#ifndef BUFFER_SIZE
# define BUFFER_SIZE 42
#endif
#include "get_next_line.h"
#include <unistd.h> //provides read
#include <stdlib.h> //provides free
#include <stdio.h> //test à supprimer

char	*resize_buffer(t_buffer *buffer)
{
	size_t	new_capacity;
	char	*new_buffer;

	new_capacity = buffer->capacity * 2;
	buffer->capacity = new_capacity;
	new_buffer = malloc(new_capacity);
	if (new_buffer == NULL)
	{
		return (NULL);
	}
	ft_memcpy(new_buffer, buffer->content, buffer->length);
	free(buffer->content);
	buffer->content = new_buffer;
	return (buffer->content);
}

char	*search_nl(int fd, t_buffer *buffer)
{
	ssize_t	byte_read;
	char	*eol_ptr;

	eol_ptr = ft_memchr(buffer->content, '\n', buffer->length);
	while (!eol_ptr)
	{
		if (buffer->capacity - buffer-> length < BUFFER_SIZE)
		{
			if (!resize_buffer(buffer))
				return (NULL);
		}
		byte_read = read(fd, buffer->content + buffer->length, BUFFER_SIZE);
		if (byte_read == -1)
			return (NULL);
		buffer->length += byte_read;
		if (byte_read > 0)
		{
			eol_ptr = ft_memchr(buffer->content, '\n', buffer->length);
			continue ;
		}
		if (buffer->length == 0)
			return (NULL);
		eol_ptr = buffer->content + buffer->length - 1;
	}
	return (eol_ptr);
}

char	*create_line(char *s, size_t n)
{
	char	*new_line;

	new_line = malloc(n + 1);
	if (new_line == NULL)
	{
		free(s);
		return (NULL);
	}
	ft_memcpy(new_line, s, n);
	new_line[n] = '\0';
	return (new_line);
}

char	*extract_line(t_buffer *buffer, char *eol_ptr)
{
	char	*new_line;
	size_t	length_nl;

	length_nl = eol_ptr - buffer->content + 1;
	new_line = malloc(length_nl + 1);
	if (new_line == NULL)
	{
		free(buffer->content);
		return (NULL);
	}
	ft_memcpy(new_line, buffer->content, length_nl);
	new_line[length_nl] = '\0';
	buffer->length -= length_nl;
	ft_memcpy(buffer->content, buffer->content + length_nl, buffer->length);
	return (new_line);
}

char	*get_next_line(int fd)
{
	static t_buffer	buffer = {NULL, BUFFER_SIZE, 0};
	char			*eol_ptr;

	if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
	{
		free(buffer.content);
		return (NULL);
	}
	if (buffer.content == NULL)
	{
		buffer.content = malloc(BUFFER_SIZE);
		if (buffer.content == NULL)
		{
			return (NULL);
		}
	}
	eol_ptr = search_nl(fd, &buffer);
	if (eol_ptr == NULL)
	{
		return (NULL);
	}
	return (extract_line(&buffer, eol_ptr));
}

/* #include <fcntl.h>
#include <stdio.h>
#include <string.h>
int main()
{
	int fd = open("test.txt", O_RDONLY);
	printf("%s",get_next_line(fd));

	close(fd);

} */