/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 16:59:26 by mmeurer           #+#    #+#             */
/*   Updated: 2025/11/05 22:46:32 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <unistd.h> //provides read and ssize_t
#include <stdlib.h> //provides size_t and free and NULL
#ifndef BUFFER_SIZE
# define BUFFER_SIZE 42
#endif

char	*checks(ssize_t bytes_read, char *stash)
{
	if (bytes_read == -1)
	{
		free(stash);
		return (NULL);
	}
	else if (bytes_read == 0)
	{
		if (stash[0] == '\0')
			return (NULL);
		return (stash);
	}
	return (stash);
}

char	*read_up_to_nl(char *stash, int fd)
{
	char	*temp;
	char	buffer[BUFFER_SIZE + 1];
	ssize_t	bytes_read;

	bytes_read = 1;
	if (stash == NULL)
		stash = ft_strdup("");
	while (bytes_read > 0 && !ft_strchr(stash, '\n'))
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (!checks(bytes_read, stash))
		{
			return (NULL);
		}
		else if (bytes_read == 0 && checks(bytes_read, stash))
		{
			return (stash);
		}
		buffer[bytes_read] = '\0';
		temp = stash;
		stash = ft_strjoin(temp, buffer);
		free(temp);
	}
	return (stash);
}

char	*set_line(char *stash)
{
	size_t	i;
	char	*line;

	i = 0;
	while (stash[i] != '\n' && stash[i] != '\0')
	{
		++i;
	}
	line = ft_substr(stash, 0, i);
	if (line == NULL)
	{
		free(stash);
		return (NULL);
	}
	return (line);
}

char	*free_stash(char *stash, size_t len_line)
{
	char	*stash_freed;

	stash_freed = ft_substr(stash, len_line + 1, ft_strlen(stash) - len_line);
	if (stash_freed == NULL)
	{
		return (NULL);
	}
	return (stash_freed);
}

char	*get_next_line(int fd)
{
	static char	*stash;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
	{
		free(stash);
		return (NULL);
	}
	stash = read_up_to_nl(stash, fd);
	if (stash == NULL)
	{
		return (NULL);
	}
	line = set_line(stash);
	stash = free_stash(stash, ft_strlen(line));
	return (line);
}

/* #include <stdio.h>
#include <fcntl.h>
int main()
{
	int fd;
	char	*s;

	fd = open("test.txt", O_RDONLY);
	while ((s = get_next_line(fd)))
	{
		puts(s);
	}
	close (fd);
} */