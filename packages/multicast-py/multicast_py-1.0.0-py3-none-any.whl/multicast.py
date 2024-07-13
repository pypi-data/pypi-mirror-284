import os
import socket
import struct

_IS_WINDOWS = os.name == 'nt'


class MulticastSocket(socket.socket):
    """
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
    """
    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        """
        Initialize multicast socket. Multicast sockets use UDP by default.
        """
        if fileno is None:
            if family == -1:
                family = socket.AF_INET
            if type == -1:
                type = socket.SOCK_DGRAM
            if proto == -1:
                proto = 0
        super().__init__(family, type, proto, fileno)

    # ====

    @property
    def reuse_addr(self) -> bool:
        """
        Get or set SO_REUSEADDR socket option.

        Default is False. Must be set before bind(). On multicast socket it allows
        two different programs to join same multicast group on same port.
        """
        return bool(self.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))

    @reuse_addr.setter
    def reuse_addr(self, value: bool):
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, int(value))

    # ====

    @property
    def multicast_ttl(self) -> int:
        """
        Get or set TTL of outgoing multicast packets.

        Default is 1 which means that multicast packets don't leave the local
        network unless the user program explicitly requests it. It is very
        important for multicast packets to set the smallest TTL possible.
        """
        return self.getsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL)

    @multicast_ttl.setter
    def multicast_ttl(self, value: int):
        self.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, value)

    # ====

    @property
    def multicast_loop(self) -> bool:
        """
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
        """
        return bool(self.getsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP))

    @multicast_loop.setter
    def multicast_loop(self, value: bool):
        self.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, int(value))

    # ====

    def get_multicast_if(self) -> str | int:
        """
        Get IP address (on POSIX) or interface index (on Windows) that used to
        send multicast packets.
        """
        data = self.getsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF)
        if _IS_WINDOWS:
            return data
        return socket.inet_ntoa(data.to_bytes(4))

    def set_multicast_if(self, address: str = "0.0.0.0", interface: int = 0):
        """
        Set IP address and interface index that used to send multicast packets.

        Specifying both address and interface options on Windows will cause
        ValueError. In you not call set_multicast_if() (or call it with default
        arguments) before sending multicast packets, default (system-dependent)
        interface will be used.
        """
        data = self._make_ip_mreq('0.0.0.0', address, interface)
        if _IS_WINDOWS:
            data = data[4:]

        self.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, data)

    # ====

    @staticmethod
    def _make_ip_mreq(group_addr, local_addr, interface):
        if not _IS_WINDOWS:
            return struct.pack("!4s4si", socket.inet_aton(group_addr), socket.inet_aton(local_addr), interface)

        local_addr = socket.inet_aton(local_addr)
        if local_addr != b'\x00\x00\x00\x00' and interface != 0:
            raise ValueError("Cannot set both local address and interface index on Windows")

        if interface != 0:
            return struct.pack("!4si", socket.inet_aton(group_addr), interface)
        return struct.pack("!4s4s", socket.inet_aton(group_addr), local_addr)

    def add_membership(self, group_addr: str, local_addr: str = "0.0.0.0", interface: int = 0):
        """
        Join to multicast group (for receiving) on specified interface.

        With default local_addr and interface will receive on all interfaces.
        """
        data = self._make_ip_mreq(group_addr, local_addr, interface)
        self.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, data)

    def drop_membership(self, group_addr: str, local_addr: str = "0.0.0.0", interface: int = 0):
        """
        Leave multicast group.

        This will revent previously done add_membership() so must be called
        with exactly same arguments as add_membership().
        """
        data = self._make_ip_mreq(group_addr, local_addr, interface)
        self.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, data)

    # ====

    @staticmethod
    def _make_ip_mreq_source(group_addr, source_addr, local_addr, interface):
        if _IS_WINDOWS:
            local_addr = socket.inet_aton(local_addr)
            if local_addr != b'\x00\x00\x00\x00' and interface != 0:
                raise ValueError("Cannot set both local address and interface index on Windows")

            if interface != 0:
                return struct.pack("!4s4si", socket.inet_aton(group_addr), socket.inet_aton(source_addr),
                                   interface)

            return struct.pack("!4s4s4s", socket.inet_aton(group_addr), socket.inet_aton(source_addr),
                               local_addr)
        else:
            if interface != 0:
                raise ValueError("interface option is supported only on Windows")

            return struct.pack("!4s4s4s", socket.inet_aton(group_addr), socket.inet_aton(local_addr),
                               socket.inet_aton(source_addr))

    def add_source_membership(self, group_addr: str, source_addr: str, local_addr: str = "0.0.0.0", interface: int = 0):
        """
        Join to multicast group for receiving only from specified source
        on specified interface.

        With default local_addr and interface will receive on all interfaces.
        Setting interface to non-zero value supported only on Windows.
        """
        data = self._make_ip_mreq_source(group_addr, source_addr, local_addr, interface)
        self.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_SOURCE_MEMBERSHIP, data)

    def drop_source_membership(self, group_addr: str, source_addr: str, local_addr: str = "0.0.0.0", interface: int = 0):
        """
        Leave multicast group for receiving only from specified source.

        This will revent previously done add_source_membership() so must
        be called with exactly same arguments as add_source_membership().
        """
        data = self._make_ip_mreq_source(group_addr, source_addr, local_addr, interface)
        self.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_SOURCE_MEMBERSHIP, data)

    def block_source(self, group_addr: str, source_addr: str, local_addr: str = "0.0.0.0", interface: int = 0):
        """
        Stop receiving multicast data from a specific source in a given group.

        This is valid only after the application has subscribed to the
        multicast group using either add_membership() or add_source_membership().
        With default local_addr and interface will receive on all interfaces.
        Setting interface to non-zero value supported only on Windows.
        """
        data = self._make_ip_mreq_source(group_addr, source_addr, local_addr, interface)
        self.setsockopt(socket.IPPROTO_IP, socket.IP_BLOCK_SOURCE, data)

    def unblock_source(self, group_addr: str, source_addr: str, local_addr: str = "0.0.0.0", interface: int = 0):
        """
        Unblock previously blocked multicast source.

        This will revent previously done block_source() so must be called
        with exactly same arguments as block_source().
        """
        data = self._make_ip_mreq_source(group_addr, source_addr, local_addr, interface)
        self.setsockopt(socket.IPPROTO_IP, socket.IP_UNBLOCK_SOURCE, data)

    # ====

    def bind_multicast(self, address: tuple[str, int]):
        """
        Bind socket to specified multicast group address and port.
        """
        address, port = address
        if _IS_WINDOWS:
            self.bind(('', port))
        else:
            self.bind((address, port))
