# gpiops2 — Raspberry Pi GPIO PS/2 experiments

Two Python experiments for reading a PS/2 keyboard through Raspberry Pi GPIO.
The original target is Raspberry Pi (2). These are user-space prototypes, not a
kernel driver or a complete PS/2 keyboard implementation.

## What is here

| File | Behavior |
| --- | --- |
| [`pui.py`](pui.py) | Polls the clock and data inputs, decodes a small hard-coded scan-code map, prints characters and emits virtual key clicks through `uinput`. |
| [`iui.py`](iui.py) | Samples on rising clock edges, collects eleven bits and prints diagnostic output for a specific character and parity check. It does not create a virtual keyboard. |

Both files use Python 2 syntax and import `RPi.GPIO` and `uinput`. They select
`GPIO.BOARD` numbering: physical pin **38** is the clock input and physical pin
**40** is the data input. These are the values in the source, not a complete
wiring guide; no circuit diagram, level-shifting design or hardware setup is
included.

## Running and stopping

There is no installer, dependency lockfile or automated test suite. On a
compatible, already configured Raspberry Pi setup, the historical entry points
are `python2 pui.py` and `python2 iui.py`. Access to GPIO is needed by both, and
`pui.py` additionally needs permission to create a Linux `uinput` device. Neither
script has command-line options; pin assignments and mappings are edited in the
source. Ctrl+C calls `GPIO.cleanup()` and exits.

Current Python, Raspberry Pi OS and keyboard compatibility have not been
verified. The polling version busy-waits on every clock transition and has no
timeout; a disconnected or stalled keyboard can keep it spinning. It emits
clicks rather than tracking a full key-down/key-up state, and the diagnostic
version is narrower still. Treat the code as a starting point for hardware
experiments, not a finished input service.
