
.PHONY: all
all: dockerfile.df
	docker build -t pandoc-thesis-v2 -f dockerfile.df .



.PHONY: clean
clean:
	docker rmi pandoc-thesis-v2
