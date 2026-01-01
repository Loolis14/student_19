# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 17:39:09 by mmeurer           #+#    #+#              #
#    Updated: 2025/12/31 10:30:41 by mmeurer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME:=push_swap

SRC:=	$(addprefix srcs/, push_swap.c) \
		$(addprefix srcs/deque/, create_and_search.c primitive_manipulations.c rotate_operations.c swap_and_push_operations.c) \
		$(addprefix srcs/parsing/, count_numbers.c parse_numbers.c) \
		$(addprefix srcs/algorithm/, checks.c sort_3.c sort_main.c) \
		$(addprefix srcs/algorithm/turk/, sort_stack_a.c push_to_the_top.c repush_stack_b.c  utils.c utils_2.c) \

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