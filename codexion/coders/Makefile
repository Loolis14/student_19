# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 21:23:53 by mmeurer           #+#    #+#              #
#    Updated: 2026/03/19 21:44:00 by mmeurer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME:=codexion

# $(addprefix srcs/, push_swap.c) \

SRC:= codexion.c parsing.c
OBJ:=$(SRC:.c=.o)

CC:=cc
CFLAGS:=-Wall -Wextra -Werror

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $^ -o $@

norm:
	norminette $(SRC)

clean:
	rm --force -- $(OBJ)

fclean: clean
	rm --force -- $(NAME)

re: fclean all

.PHONY: clean fclean re all norm 