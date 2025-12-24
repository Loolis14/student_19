/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 17:39:20 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/24 11:58:09 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/* #include "push_swap.h"
#include <stdio.h> //ssize_t à supprimer ! */

/* int main(int argc, char **argv)
{
	ssize_t count;
	t_deque	*a;
	t_deque	*b;

	if (argc == 1 || argv[1][0] == '\0')
	{
		return (0);
	}
	count = count_numbers(argv + 1);
	if (count == -1 || count == 0)
	{
		printf("%s", "Error\n");
		return (0);
	}
	printf("count = %zi\n", count);
	a = create_t_deque(count, 'a');
	if (!parse_numbers(argv + 1, a))
	{
		printf("%s", "Error\n");
		//free(a); à faire
		return (0);
	}
	if (!check_duplicate(a))
	{
		printf("%s", "Error\n");
		//free(a); à faire
		return (0);
	}
	if (!is_sorted(a))
	{
		b = create_t_deque(count, 'b');
		dispatch_by_length(a, b);
		//free(a); à faire
		//free(b); à faire
	}
	else
	{
		//free(a); à faire
		return (0);
	}
	
	//print les nombres
	size_t i= 0;
	printf("taille b %zi\n", b->length);
	while (i < b->length)
	{
		printf("deque b %i\n", b->numbers[(b->front + i) % b->capacity]);
		++i;
	}
	printf("taille a %zi\n", a->length);
	i = 0;
	while (i < a->length)
	{
		printf("deque a %i\n", a->numbers[(a->front + i) % a->capacity]);
		++i;
	}
}
 */