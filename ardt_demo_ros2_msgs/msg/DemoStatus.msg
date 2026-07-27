# Current state of the demo counter.

# Time of the last update.
builtin_interfaces/Time stamp
# Current counter value.
int64 count
# One of the STATE_* constants below.
uint8 state 0

uint8 STATE_IDLE=0      # no goal active
uint8 STATE_COUNTING=1  # a CountTo goal is running
