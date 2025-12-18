# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 17:39:09 by mmeurer           #+#    #+#              #
#    Updated: 2025/12/13 17:53:56 by mmeurer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME:=push_swap.a

SRC:=push_swap.c
OBJ:=$(SRC:.c=.o)

CC:=cc
CFLAGS:=-Wall -Werror -Wextra

all: $(NAME)

$(NAME): $(OBJ)
	ar rsc $(NAME) $(OBJ)

%.o: %.c
	$(CC) $(CFLAGS) -c $^ -o $@

clean:
	rm --force -- $(OBJ)

fclean: clean
	rm --force -- $(NAME)

re: fclean all

.PHONY: clean fclean re all