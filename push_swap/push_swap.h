/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 17:48:17 by mmeurer           #+#    #+#             */
/*   Updated: 2025/12/18 21:31:13 by mmeurer          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stddef.h>
# include <unistd.h>

//struct de l'arr
typedef struct{
	int	*numbers; //store elements
	int capacity; //max size
	int	front; //index of the front element
	int	size; //current number of element
}	stack;

int	ft_printf(const char *format, ...);


//count numbers
ssize_t 	count_numbers(char **argv);

//parser
int	*parse_numbers(char **args, ssize_t count);


//utils
int	is_digit(char c);
int	is_space(char c);
int	ft_strncmp(const char *s1, const char *s2, size_t n);
int	ft_atoi(const char *nptr);

//a supprimer
#include <stdio.h>

# endif //PUSH_SWAP_H
