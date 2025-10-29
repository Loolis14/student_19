/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:38:44 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:42:19 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list
#include <stdlib.h> //provides free and NULL

void	ft_lstdelone(t_list *lst, void (*del)(void *))
{
	if (lst == NULL)
	{
		return ;
	}
	del(lst -> content);
	free(lst);
}

/* #include <stdio.h>
void	del(void *content)
{
	puts(content);
}


int main()
{
	t_list	*a;
	a = ft_lstnew("shrek");
	t_list	*b;
	b = ft_lstnew("is");
	t_list	*c;
	c = ft_lstnew("real");
	t_list	**test;

	test = &a;
	ft_lstadd_back(test, b);
	ft_lstadd_back(test, c);
	ft_lstdelone(b, del);
	while (*test != NULL)
	{
		puts((char *)(*test)->content);
		*test = (*test)->next;
	}
} */