/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:39:16 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:42:34 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list
#include <stddef.h>
#include <stdlib.h> //provides malloc and NULL and free

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new;
	t_list	*temp;

	new = ft_lstnew(f(lst ->content));
	if (new == NULL)
	{
		ft_lstclear(&new, del);
		return (NULL);
	}
	lst = lst -> next;
	while (lst != NULL)
	{
		temp = ft_lstnew(f(lst ->content));
		if (temp == NULL)
		{
			ft_lstclear(&new, del);
			return (NULL);
		}
		ft_lstadd_back(&new, temp);
		lst = lst -> next;
	}
	return (new);
}

/* #include <stdio.h>
void	*f(void *content)
{
	(void)content;
	return ("shrek");
}

void	del(void *content)
{
	content = NULL;
}

int main()
{
	//shrek shrek shrek
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
	t_list	*d;
	d = ft_lstmap(*test, f, del); 
	
	while (d != NULL)
	{
		puts((char *)d->content);
		d = d->next;
	}
} */