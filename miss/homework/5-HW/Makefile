# Turns each supplied poem into the mocking spongebob meme and creates an html page to display it


INPUTS = $(shell find . -type f -name '*.txt') 
OUTPUTS = $(INPUTS:.txt=.html)

.PHONY: all
all: $(OUTPUTS) 
	@for file in $(OUTPUTS); do\
		touch $$file;\
	done

%.html: %.txt  
	@echo "<head>\n</head>\n<body>\n<img src="spongemock.jpg">\n<PRE>\n" > $@	
	@cat $< | sed 's:\([A-Za-z]\)\([A-Za-z]\):\L\1\U\2:g' >> $@
	@echo "</PRE>\n</body>" >> $@


.PHONY: clean
clean:
	rm $(OUTPUTS)


.PHONY: rebuild
rebuild:
	$(MAKE) clean
	$(MAKE) all
