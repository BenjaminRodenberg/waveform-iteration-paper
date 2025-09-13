DIRS := oscillator-overlap/Fig10 oscillator-overlap/Fig11

.PHONY: all $(MAKECMDGOALS) $(DIRS)
$(MAKECMDGOALS) all: $(DIRS)

$(DIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)
