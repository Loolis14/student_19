# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 17:39:09 by mmeurer           #+#    #+#              #
#    Updated: 2025/12/30 20:39:33 by mmeurer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME:=push_swap

SRC:=	$(addprefix src/deque_functions/, deque_manipulations.c primitive_functions.c rotate_operations.c swap_and_push_operations.c) \
		$(addprefix src/parse_numbers/, count_numbers.c parse_numbers.c) \
		$(addprefix src/, push_swap.c) \
		$(addprefix src/tri_functions/, checks.c sort_3.c sort_4.c sort_main.c) \
		$(addprefix src/turk/, algorithm_utils.c push_to_the_top.c repush_stack_b.c sort_stack_a.c) \

OBJ:=$(SRC:.c=.o)

CC:=cc
CFLAGS:=-Wall -Werror -Wextra
CPPFLAGS := -I.

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(LDFLAGS) $(OBJ) $(LDLIBS) -o $@

%.o: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $^ -o $@

compile_commands.json: fclean
	bear -- $(MAKE) all

clean:
	rm --force -- $(OBJ)

fclean: clean
	rm --force -- $(NAME)

re: fclean all

.PHONY: clean fclean re all