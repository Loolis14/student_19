/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 17:48:17 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/30 23:59:14 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stddef.h>
# include <unistd.h>
# include <stdbool.h>

typedef struct{
	int		*numbers;
	size_t 	capacity;
	size_t	front;
	size_t	length;
	char	tag;
}	t_deque;

t_deque		*create_t_deque(int count, char tag);
int			deque_at(t_deque *deque, size_t i);

//parse numbers
ssize_t 	count_numbers(char **argv);
bool		parse_numbers(char **args, t_deque *a);

//tri control
bool		is_sorted(t_deque *deque);
bool		check_duplicate(t_deque *deque);

//deque manipulations
void		push_front(t_deque *deque, int value);
void		push_back(t_deque *deque, int value);
int			pop_front(t_deque *deque);
int			pop_back(t_deque *deque);

//possibles operations
void		swap_one(t_deque *deque);
void		swap_both(t_deque *a, t_deque *b);
void		rotate_one(t_deque *deque);
void		rotate_both(t_deque *a, t_deque *b);
void		reverse_rotate_one(t_deque *deque);
void		reverse_rotate_both(t_deque *a, t_deque *b);
void		push_queue(t_deque *to_push, t_deque *to_pop);

//tri
void		dispatch_by_length(t_deque *a, t_deque *b);
void		sort_3(t_deque *deque);
void		sort_4(t_deque *a, t_deque *b);
//void		turk(t_deque *a, t_deque *b);

//turk algorithm
void		sort_stack_a(t_deque *a, t_deque *b);
void		repush_stack_b(t_deque *a, t_deque *b);

//algorithm utils
typedef struct{
	size_t	index_a;
	size_t	index_b;
	size_t	cost;
}	t_target;

typedef struct{
	int		min;
	size_t	index_min;
	int		max;
	size_t	index_max;
}	limits;

size_t		limits_idx_value(t_deque *deque, char c);
size_t		calculate_cost(size_t index_of_b, size_t index_of_a, size_t length_a, size_t length_b);
void    	to_the_top(t_deque *a, t_deque *b, t_target *target);
void    	rotate_by_one(t_deque *stack, ssize_t rotations);
ssize_t		number_of_rotations(size_t index, size_t length);
size_t		ft_max(size_t a, size_t b);

//utils
int			ft_atoi(const char *nptr);
int			is_space(char c);
int			is_digit(char c);
int			ft_free(t_deque *deque);

# endif //PUSH_SWAP_H
