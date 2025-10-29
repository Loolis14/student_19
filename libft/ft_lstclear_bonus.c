/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:38:27 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:42:14 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list and ft_lstdelone
#include <stdlib.h>

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*temp;
	t_list	*next;

	temp = *lst;
	while (temp != NULL)
	{
		next = temp -> next;
		ft_lstdelone(temp, del);
		temp = next;
	}
	*lst = NULL;
}

/* #include <stdio.h>
void	del(void *content)
{
	puts("shrek");
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
	ft_lstclear(test, del);
	while (*test != NULL)
	{
		puts((char *)(*test)->content);
		*test = (*test)->next;
	}
} */