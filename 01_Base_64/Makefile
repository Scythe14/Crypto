CC = gcc
RM = rm -f

CXXFLAGS += -Wall -Wextra -Werror

COLOR_OFF = \033[0m
COLOR_ON = \033[32;01m

PROG =	$(COLOR_ON) [/_\ 01 Challenge Compiled /_\] $(COLOR_OFF)
NAME = challenge

SRC =	main.c

OBJ = $(SRC:.c=.o)

all: $(NAME) $(GENNAME)

$(NAME): $(OBJ)
	$(CC) $(OBJ) -o $(NAME)
	@echo "$(PROG)"

clean:
	$(RM) $(OBJ)

fclean: clean
	$(RM) $(NAME)

re: clean fclean all

.PHONY: all clean fclean re
