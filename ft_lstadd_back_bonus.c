/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:38:09 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 15:13:16 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list

void	ft_lstadd_back(t_list **lst, t_list *node)
{
	t_list	*last;

	if (!node || !lst)
	{
		return ;
	}
	if (!*lst)
	{
		*lst = node;
		return ;
	}
	else
	{
		last = ft_lstlast(*lst);
		last -> next = node;
	}
	return ;
}

/* #include <stdio.h>
int main()
{
	//a, a, a, shrek
	char	*shrek = "a";
	t_list a = {shrek, NULL};
	t_list b = {shrek, NULL};
	t_list c = {shrek, NULL};
	a.next = &b;
	b.next = &c;

	t_list	*e = &a;

	char *s = "shrek";
	t_list *d;
	d = ft_lstnew(s);

	ft_lstadd_back(&e,d);

	while (e != NULL)
	{
		puts((char *)e->content);
		e = e->next;
	}
} */