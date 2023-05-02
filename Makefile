##
## EPITECH PROJECT, 2022
## python 
## File description:
## makefile
##

all:
	cp groundhog.py groundhog
	chmod +x groundhog

clean:

fclean: clean
	rm groundhog
	rm -rf __pycache__

re: fclean all
