DIRS := oscillator-overlap partitioned-heat-conduction perpendicular-flap

.PHONY: all $(MAKECMDGOALS) $(DIRS)
$(MAKECMDGOALS) all: $(DIRS)

$(DIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)
