/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:42:43 by mmeurer           #+#    #+#             */
/*   Updated: 2025/10/27 10:42:44 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h" //provides t_list
#include <stdlib.h> //provides NULL

int	ft_lstsize(t_list *lst)
{
	int	count;

	count = 0;
	while (lst != NULL)
	{
		++count;
		lst = lst -> next;
	}
	return (count);
}

/* #include <stdio.h>
int main()
{
	int shrek = 1;
	t_list a = {&shrek, NULL};
	t_list b = {&shrek, NULL};
	t_list c = {&shrek, NULL};
	t_list d = {&shrek, NULL};
	a.next = &b;
	b.next = &c;
	c.next = &d;

	printf("%i\n", ft_lstsize(&a)); //4

} */