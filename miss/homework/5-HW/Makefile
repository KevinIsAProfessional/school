INPUTS := $(shell find . -type f -name '*.txt')
OUTPUTS := $(INPUTS:.*.txt=.mocking.txt)

.PHONY: build
build: ${OUTPUTS}



.PHONY: clean
clean:
	@rm -f ${OUTPUTS}


%.mocking.txt: %.txt 
	echo "mocking $<"
	cat $<
