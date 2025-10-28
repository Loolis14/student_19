/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:39:24 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:42:38 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list
#include <stdlib.h> //provides malloc and NULL

t_list	*ft_lstnew(void *content)
{
	t_list	*elem;

	elem = malloc(sizeof(t_list));
	if (elem == NULL)
	{
		return (NULL);
	}
	elem -> content = content;
	elem -> next = NULL;
	return (elem);
}

/* #include <stdio.h>
int main()
{
	char *s = "shrek";
	t_list *head = ft_lstnew(s);

	printf("%s\n", (char *)head->content);
} */