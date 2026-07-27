# Emitted for every counter step (see the CountTo action).

# Time the step was taken.
builtin_interfaces/Time stamp
int64 before  # value before the step
int64 after   # value after the step

# What triggered the step: one of the REASON_* constants.
uint8 reason

uint8 REASON_TICK=0     # the periodic timer
uint8 REASON_SERVICE=1  # a SetCounter call
uint8 REASON_ACTION=2   # an active CountTo goal
