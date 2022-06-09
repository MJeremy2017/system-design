# User Model vs. Kernel Mode

## User Model
When a user boot up the computer, he would land in user mode. User model has lower priority and is not allowed
to access system resources directly.


## Kernel Model

Kernel model has very high priority and is in charge of communication between software and hardware. When a
user issue a command to access hardware (e.g. turn on a camera), it needs to switch to kernel mode and then
switch back to user mode.