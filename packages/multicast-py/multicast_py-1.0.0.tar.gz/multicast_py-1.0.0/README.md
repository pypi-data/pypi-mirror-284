# multicast.py

Low-to-mid level wrapper for multicast sockets. Simple and cross-platform.

The library is typed, but if you want: [DOCS HERE](https://gitlab.neko-dev.ru/me/multicast-py/-/blob/main/DOCS.md).

## Installation

```sh
pip install multicast_py
```

## Usage 

Creation socket to send multicast packets:

```python
s = MulticastSocket()
s.multicast_ttl = 2  # if needed
s.multicast_loop = False  # if needed, POSIX only (on Windows does nothing)
s.set_multicast_if(address='192.168.0.101')  # local ip, used almost always

s.sendto(b'Multicast message', (group_address, group_port))  # send multicast message
```

Creation socket to receive multicast packets:

```python
s = MulticastSocket()
s.reuse_addr = True  # if needed
s.multicast_loop = False  # if needed, Windows only (on POSIX does nothing)
s.bind_multicast((group_address, group_port))
s.add_membership(group_address)  # also can specify local address

data = s.recvfrom(1024)  # receive multicast message
```

## License

MIT License. Full test available in LICENSE file.
