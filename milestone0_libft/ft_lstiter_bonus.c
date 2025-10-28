/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:38:51 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:42:24 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	while (lst != NULL)
	{
		f(lst -> content);
		lst = lst -> next;
	}
}

/* #include <stdio.h>
void	plus(void *content)
{
	content += 1;
	puts(content);
}

int	main()
{
	//hrek s eal
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
	ft_lstiter(*test, plus);
	while (*test != NULL)
	{
		puts((char *)(*test)->content);
		*test = (*test)->next;
	}
} */