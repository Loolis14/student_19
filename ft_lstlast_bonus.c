/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:39:08 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 15:06:41 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list
#include <stdlib.h> //provides NULL

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
	{
		return (NULL);
	}
	while (lst -> next != NULL)
	{
		lst = lst -> next;
	}
	return (lst);
}

/* #include <stdio.h>
int main()
{
	//fin
	char	*shrek = "a";
	char	*shrek1 = "fin";
	t_list a = {shrek, NULL};
	t_list b = {shrek, NULL};
	t_list c = {shrek1, NULL};
	a.next = &b;
	b.next = &c;

	t_list *d = ft_lstlast(&a);
	puts(d-> content);
} */