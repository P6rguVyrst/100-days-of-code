import socket
from struct import unpack
from binascii import unhexlify, hexlify


class HeaderFactory(object):

    def eth_header(self, data):
        """Return ethernet header"""
        storeobj = data
        storeobj = unpack('!6s6sH', storeobj)

        dest_mac = hexlify(storeobj[0])
        src_mac = hexlify(storeobj[1])
        eth_protocol = socket.ntohs(storeobj[2])

        header = dict(
            source = dict(
                mac = src_mac,
            ),
            destination = dict(
                mac = dest_mac,

            ),
            protocol = eth_protocol
        )
        return header

    def ip_header_length(self, ip_header_version):
        version = ip_header_version >> 4 # what to do with version?
        ihl = ip_header_version & 0xF
        iph_length = ihl * 4
        return iph_length
    def tcp_header_length(self, offset):
        return offset >> 4

    def ip_header(self, data):
        """Return IP header"""
        iph = unpack('!BBHHHBBH4s4s', data)

        header = dict(
            version = iph[0],
            tos = iph[1],
            total_length = iph[2],
            id = iph[3],
            frag_offset = iph[4],
            ttl = iph[5],
            protocol = iph[6],
            header_checksum = iph[7],
            src_addr = socket.inet_ntoa(iph[8]),
            dest_addr = socket.inet_ntoa(iph[9]),
        )
        header['length'] = self.ip_header_length(header['version'])
        return header

    def icmp_header(self, data):
        """Return ICMP header"""
        icmph = unpack('!BBH', data)
        icmp_type = icmph[0]
        code = icmph[1]
        checksum = icmph[2]

        header = dict(
            icmp_type = icmp_type,
            code = code,
            checksum = checksum,
        )
        return header

    def tcp_header(self, data):
        """Return TCP header"""
        tcph = unpack('!HHLLBBHHH', data)
        header = dict(
            src_port = tcph[0],
            dest_port = tcph[1],
            sequence = tcph[2],
            acknowledgement = tcph[3],
            offset_reserved = tcph[4],
            tcp_flag = tcph[5],
            window = tcph[6],
            checksum = tcph[7],
            urgent_pointer = tcph[8],
        )
        header['length'] = self.ip_header_length(header['offset_reserved'])
        return header

    def udp_header(self, data):
        udph = unpack('!HHHH', data)
        header = dict(
            source_port = udph[0],
            dest_port = udph[1],
            length = udph[2],
            checksum = udph[3],
        )
        return header


class NetworkTraffic(object):

    def __init__(self):
        self.sock = self._connect()
        self.unpack = HeaderFactory()

    def _connect(self):
        try:
            sock = socket.socket(
                socket.AF_PACKET,
                socket.SOCK_RAW,
                socket.ntohs(0x0003),
            )
            return sock
        except socket.error as err:
            print(err)
            sys.exit(1)

    def capture(self):
        while True:
            packet = self.sock.recvfrom(65565)
            self.analyze(packet)

    def extract_data(self, packet, header_size):
        data_size = len(packet) - header_size
        data = packet[header_size:]
        return data

    def analyze(self, packet):
        packet = packet[0]
        eth_length = 14
        eth_header = packet[:eth_length]
        eth = self.unpack.eth_header(eth_header)
        if eth['protocol'] == 8:
            ip_header = packet[eth_length: eth_length+20]
            ip_data = self.unpack.ip_header(ip_header)
            protocol = ip_data['protocol']
            ip_packet_len = eth_length + ip_data['length']
            if protocol == 6:
                tcp = ip_packet_len
                header_len = 20
                tcp_header = packet[tcp: tcp+header_len]
                header = self.unpack.tcp_header(tcp_header)
                h_size = ip_packet_len + header['length'] * 4
                data = self.extract_data(packet, h_size)
            elif protocol == 1:
                icmp = ip_packet_len
                header_len = 4
                icmp_header = packet[icmp: icmp+header_len]
                header = self.unpack.icmp_header(icmp_header)
                h_size = ip_packet_len + header_len
                data = self.extract_data(packet, h_size)
            elif protocol == 17:
                udp = ip_packet_len
                header_len = 8
                udp_header = packet[udp: udp+header_len]
                header = self.unpack.udp_header(udp_header)
                h_size = ip_packet_len + header_len
                data = self.extract_data(packet, h_size)
            #print(type(data), data)
            #print(f'{header}')
        else:
            # packet type 1544, 56710
            print(f'Not IP traffic: {eth}')


NWK = NetworkTraffic()


if __name__ == '__main__':
    NWK.capture()
