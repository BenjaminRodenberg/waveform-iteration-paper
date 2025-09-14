DIRS := oscillator-overlap/Fig10 oscillator-overlap/Fig11 oscillator-overlap/Tab1

.PHONY: all $(MAKECMDGOALS) $(DIRS)
$(MAKECMDGOALS) all: $(DIRS)

$(DIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)
