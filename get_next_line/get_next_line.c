#include <unistd.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#define BUFFER_SIZE 42

//file or standart input
size_t	ft_strlen(const char *str)
{
	size_t	len;

	len = 0;
	while (str[len])
	{
		++len;
	}
	return (len);
}

size_t	ft_strlcpy(char *dst, const char *src, size_t sz)
{
	size_t	i;

	i = 0;
	if (sz > 0)
	{
		while ((i + 1 < sz) && src[i])
		{
			dst[i] = src[i];
			++i;
		}
		dst[i] = '\0';
	}
	return (ft_strlen(src));
}

char	*ft_strchr(const char *s, int c)
{
	c = (unsigned char) c;
	while (*s)
	{
		if (*s == c)
		{
			return ((char *) s);
		}
		++s;
	}
	if (c == '\0')
	{
		return ((char *) s);
	}
	return (NULL);
}

char	*get_next_line(int fd)
{
	static char buffer[BUFFER_SIZE];
	char *line;
	ssize_t	bytes_read;
	int	i;

	line = malloc(18);
	if (line == NULL)
	{
		return (NULL);
	}
	i = 0;
	bytes_read = read(fd, buffer, sizeof buffer);
	while (bytes_read > 0) //valable pour une seule ligne
	{
		bytes_read = read(fd, buffer, sizeof buffer);
		line[i] = buffer[0];
		++i;
		if (buffer[0] == '\n')
		{
			break;
		}
		//si no \n -> buffer pas assez grand
	}
	if (bytes_read < 0)
	{
		return (NULL);
	}
	if (bytes_read == 0) //fin du fichier
	line[i] = '\0';
	return (line);
	//Erro occurred return NULL or nothing else to read
	//loop to read each line => \n and each time i have to return the line with \n (except for the end of the doc if this one doesn't 
	// end with \n)

}

#include <stdio.h>
#include <fcntl.h>
int main()
{
	int fd;

	fd = open("test.txt", O_RDONLY);
	puts(get_next_line(fd));	//1
	puts(get_next_line(fd));
	puts(get_next_line(fd));
	close (fd);
}
