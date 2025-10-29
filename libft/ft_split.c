/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:44:45 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:45:04 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h> //provides size_t
#include <stdlib.h> //provides NULL and malloc

static int	is_sep(char s, char c)
{
	if (s == c)
	{
		return (1);
	}
	return (0);
}

static int	count_words(char const *s, char c)
{
	size_t	words;
	size_t	i;

	i = 0;
	words = 0;
	while (s[i])
	{
		if (is_sep(s[i], c) == 0)
		{
			++words;
			while (s[i] && is_sep(s[i], c) == 0)
			{
				++i;
			}
		}
		else
		{
			++i;
		}
	}
	return (words);
}

static char	*words_split(char const *s, char c)
{
	char	*word;
	size_t	i;

	i = 0;
	while (s[i] && is_sep(s[i], c) == 0)
	{
		++i;
	}
	word = malloc(i + 1);
	if (word == NULL)
		return (NULL);
	i = 0;
	while (s[i] && is_sep(s[i], c) == 0)
	{
		word[i] = s[i];
		++i;
	}
	word[i] = '\0';
	return (word);
}

static void	*free_all(char **words, size_t i)
{
	while (i != 0)
	{
		free(words[i]);
		--i;
	}
	free(words);
	return (NULL);
}

char	**ft_split(char const *s, char c)
{
	char	**words;
	size_t	i;

	words = malloc((sizeof (char *)) * (count_words(s, c) + 1));
	if (words == NULL)
		return (NULL);
	i = 0;
	while (*s)
	{
		if (is_sep(*s, c) == 0)
		{
			words[i] = words_split(&*s, c);
			if (words[i] == NULL)
				free_all(words, i);
			++i;
			while (*s && is_sep(*s, c) == 0)
				++s;
		}
		else
			++s;
	}
	words[i] = NULL;
	return (words);
}

/* #include <stdio.h>

int main()
{
	char s[] = "shrek is real";
	char **d;
	d = ft_split(s, ' ');
	while (*d != NULL)
	{
		puts(*d);
		++d;
	}
}
 */