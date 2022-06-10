# Swap Space

Swap space is used when the physical memory(RAM) is full. In this case, if more memory is needed, some
inactive files will be stored in swap space.

Swap space is located on hard drive, so accessing to them is slower than accessing memory.

`M = Amount of RAM in GB, and S = Amount of swap in GB, then`

```
If M < 2
	S = M *2
Else
	S = M + 2
```