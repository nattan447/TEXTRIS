all : documentacao programa
.PHONY : programa

documentacao :
	doxygen Doxyfile
	clear


programa :
	python3 main.py