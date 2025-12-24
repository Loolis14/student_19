/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 17:48:17 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/24 16:26:18 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stddef.h>
# include <unistd.h>
# include <stdbool.h>
#include <stdio.h>

typedef struct{
	int		*numbers; 	//store elements
	size_t 	capacity; 	//max size
	size_t	front; 		//index of the front element
	size_t	length; 	//current number of element
	char	tag; 		//a or b
	bool	cost_calcul;
}	t_deque;

t_deque		*create_t_deque(int count, char tag);
int			deque_at(t_deque *deque, size_t i);

//parse numbers
ssize_t 	count_numbers(char **argv);
bool		parse_numbers(char **args, t_deque *a);

//deque manipulations
void		push_front(t_deque *deque, int value);
void		push_back(t_deque *deque, int value);
int			pop_front(t_deque *deque);
int			pop_back(t_deque *deque);

//possibles operations
void		swap_one(t_deque *a);
void		swap_both(t_deque *a, t_deque *b);
void		rotate_one(t_deque *a);
void		rotate_both(t_deque *a, t_deque *b);
void		reverse_rotate_one(t_deque *a);
void		reverse_rotate_both(t_deque *a, t_deque *b);
void		push_queue(t_deque *to_push, t_deque *to_pop);

//tri
bool		is_sorted(t_deque *deque);
bool		check_duplicate(t_deque *deque);

void		dispatch_by_length(t_deque *a, t_deque *b);
void		sort_3(t_deque *deque);
void		sort_4(t_deque *a, t_deque *b);
void		sort_5(t_deque *a, t_deque *b);

typedef struct{
	int		min;
	size_t	index_min;
	int		max;
	size_t	index_max;
}	limits;
limits		find_limits(t_deque *a);

typedef struct{
	int		number_in_a;
	size_t	index_a;
	int		number_in_b;
	size_t	index_b;
	size_t	cost;
}	t_target;

void		turk_algorithm(t_deque *a, t_deque *b);
size_t		calculate_cost(size_t index_of_b, size_t index_of_a, size_t length_a, size_t length_b);
void		sort_stack_a(t_deque *a, t_deque *b);

//utils
int			ft_atoi(const char *nptr);
int			is_space(char c);
int			is_digit(char c);
int			ft_printf(const char *format, ...); // a ajouter et changer dans le reste avec ma propre fonction ??

//a supprimer

# endif //PUSH_SWAP_H
