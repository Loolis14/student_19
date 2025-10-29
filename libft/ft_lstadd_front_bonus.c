/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:38:17 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:42:07 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list

void	ft_lstadd_front(t_list **lst, t_list *node)
{
	node -> next = *lst;
	*lst = node;
}

/* #include <stdio.h>
int main()
{
	//shrek is real
	char *s = "shrek";
	char *p = "is";
	char *q = "real";
	t_list	*a;
	t_list	*b;
	a = ft_lstnew(p);
	b = ft_lstnew(s);
	ft_lstadd_front(&a, b);
	while (a != NULL)
	{
		puts((char *)a->content);
		a = a->next;
	}
} */