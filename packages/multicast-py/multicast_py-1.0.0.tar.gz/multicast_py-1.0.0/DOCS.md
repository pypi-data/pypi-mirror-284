# multicast

## MulticastSocket Objects

```python
class MulticastSocket(socket.socket)
```

Multicast socket class.

Creation socket to send multicast packets:
```python
s = MulticastSocket()
s.multicast_ttl = 2  # if needed
s.multicast_loop = False  # if needed, POSIX only
s.set_multicast_if(address='192.168.0.101')  # local ip, used almost always

s.sendto(b'Multicast message', (group_address, group_port))  # send multicast message
```

Creation socket to receive multicast packets:
```python
s = MulticastSocket()
s.reuse_addr = True  # if needed
s.multicast_loop = False  # if needed, Windows only
s.bind_multicast((group_address, group_port))
s.add_membership(group_address)  # also can specify local address

data = s.recvfrom(1024)  # receive multicast message
```

### \_\_init\_\_

```python
def __init__(family=-1, type=-1, proto=-1, fileno=None)
```

Initialize multicast socket. Multicast sockets use UDP by default.

### reuse\_addr

```python
@property
def reuse_addr() -> bool
```

Get or set SO_REUSEADDR socket option.

Default is False. Must be set before bind(). On multicast socket it allows
two different programs to join same multicast group on same port.

### multicast\_ttl

```python
@property
def multicast_ttl() -> int
```

Get or set TTL of outgoing multicast packets.

Default is 1 which means that multicast packets don't leave the local
network unless the user program explicitly requests it. It is very
important for multicast packets to set the smallest TTL possible.

### multicast\_loop

```python
@property
def multicast_loop() -> bool
```

When using one socket to send and receive multicast packets and
no other program bound to this multicast group and port: Disable
to prevent looping back multicast packets that we sent from being
received by this socket.

When using separate sockets to send and receive multicast packets
or when reuse_addr is true and other programs bound to this multicast
group and port: Platform-dependent as following:

Windows: Disable to prevent receiving outgoing multicast packets
from local machine.

POSIX: Disable to prevent multicast packets that we sent from being
received by local machine.

Default is True. When set to False we will not receive multicast
packets that we sent.

### get\_multicast\_if

```python
def get_multicast_if() -> str | int
```

Get IP address (on POSIX) or interface index (on Windows) that used to
send multicast packets.

### set\_multicast\_if

```python
def set_multicast_if(address: str = "0.0.0.0", interface: int = 0)
```

Set IP address and interface index that used to send multicast packets.

Specifying both address and interface options on Windows will cause
ValueError. In you not call set_multicast_if() (or call it with default
arguments) before sending multicast packets, default (system-dependent)
interface will be used.

### add\_membership

```python
def add_membership(group_addr: str,
                   local_addr: str = "0.0.0.0",
                   interface: int = 0)
```

Join to multicast group (for receiving) on specified interface.

With default local_addr and interface will receive on all interfaces.

### drop\_membership

```python
def drop_membership(group_addr: str,
                    local_addr: str = "0.0.0.0",
                    interface: int = 0)
```

Leave multicast group.

This will revent previously done add_membership() so must be called
with exactly same arguments as add_membership().

### add\_source\_membership

```python
def add_source_membership(group_addr: str,
                          source_addr: str,
                          local_addr: str = "0.0.0.0",
                          interface: int = 0)
```

Join to multicast group for receiving only from specified source
on specified interface.

With default local_addr and interface will receive on all interfaces.
Setting interface to non-zero value supported only on Windows.

### drop\_source\_membership

```python
def drop_source_membership(group_addr: str,
                           source_addr: str,
                           local_addr: str = "0.0.0.0",
                           interface: int = 0)
```

Leave multicast group for receiving only from specified source.

This will revent previously done add_source_membership() so must
be called with exactly same arguments as add_source_membership().

### block\_source

```python
def block_source(group_addr: str,
                 source_addr: str,
                 local_addr: str = "0.0.0.0",
                 interface: int = 0)
```

Stop receiving multicast data from a specific source in a given group.

This is valid only after the application has subscribed to the
multicast group using either add_membership() or add_source_membership().
With default local_addr and interface will receive on all interfaces.
Setting interface to non-zero value supported only on Windows.

### unblock\_source

```python
def unblock_source(group_addr: str,
                   source_addr: str,
                   local_addr: str = "0.0.0.0",
                   interface: int = 0)
```

Unblock previously blocked multicast source.

This will revent previously done block_source() so must be called
with exactly same arguments as block_source().

### bind\_multicast

```python
def bind_multicast(address: tuple[str, int])
```

Bind socket to specified multicast group address and port.

