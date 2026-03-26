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

SRC:= codexion.c parsing.c threads.c utils.c
OBJ:=$(SRC:.c=.o)

CC:=cc
CFLAGS:=-Wall -Wextra -Werror
THREAD=-pthread

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(THREAD) $(OBJ) -o $@

%.o: %.c
	$(CC) $(CFLAGS) $(THREAD) -c $^ -o $@

norm:
	norminette $(SRC)

clean:
	rm -f -- $(OBJ)

fclean: clean
	rm -f -- $(NAME)

re: fclean all

.PHONY: clean fclean re all norm 