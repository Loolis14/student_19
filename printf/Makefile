# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmeurer <mmeurer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/29 23:08:41 by mmeurer           #+#    #+#              #
#    Updated: 2025/11/05 13:39:53 by mmeurer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME:=libftprintf.a

SRC:= ft_printf.c cases_char.c cases_digit.c cases_utils.c
OBJ:=$(SRC:.c=.o)

CC:=cc
CFLAGS:=-Wall -Wextra -Werror

all: $(NAME)

$(NAME): $(OBJ)
		ar rcs $(NAME) $(OBJ)

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
