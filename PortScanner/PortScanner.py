# -*- coding: utf-8 -*-

import socket
import platform
import threading
import time

from etc import constants


class PortScanner:
    # default ports to be scanned is top 1000
    __port_list_top_1000 = constants.port_list_top_1000
    __port_list_top_100 = constants.port_list_top_100
    __port_list_top_50 = constants.port_list_top_50

    # default thread number limit
    __thread_limit = 1000

    # default connection timeout time in seconds
    __delay = 10


    @classmethod
    def __usage(cls):
        """
        Return the usage information for invalid input host name.
        """
        print('python Port Scanner v0.1')
        print('please make sure the input host name is in the form of "something.com" or "http://something.com!"\n')

    def __init__(self, target_ports=None):
        """
        Constructor of a PortScanner object. If target_ports is a list, this list of ports will be used as
        the port list to be scanned. If the target_ports is a int, it should be 50, 100 or 1000, indicating
        which default list will be used.

        :param target_ports: if this args is a list, then this list of ports that is going to be scanned,
        default to self.__port_list_top_1000. if this args is an int, then it should be 50, 100 or 1000. And
        the corresponding default list will be used respectively.
        :type target_ports: list or int
        """
        if target_ports is None:
            self.target_ports = self.__port_list_top_1000
        elif type(target_ports) == list:
            self.target_ports = target_ports
        elif type(target_ports) == int:
            self.target_ports = self.check_default_list(target_ports)

    def check_default_list(self, target_port_rank):
        """
        Check the input target port rank. The target port rank should be 50, 100 or 1000.
        And for a valid input, corresponding port list will be returned.

        :param target_port_rank: top K commonly used port list to be returned.
        :return: top K commonly used port list.
        """
        if (
            target_port_rank != 50 and
            target_port_rank != 100 and
            target_port_rank != 1000
        ):
            raise ValueError(
                'Invalid port rank {}. Should be 50, 100 or 1,000.'.format(target_port_rank)
            )

        if target_port_rank == 50:
            return self.__port_list_top_50
        elif target_port_rank == 100:
            return self.__port_list_top_100
        else:
            return self.__port_list_top_1000

    def scan(self, host_name, message=''):
        """
        This is the function need to be called to perform port scanning

        :param host_name: the hostname that is going to be scanned
        :param message: the message that is going to be included in the scanning packets
        in order to prevent ethical problem (default: '').
        :return: a dict object containing the scan results for a given host in the form of
        {port_number: status}
        :rtype: dict
        """
        host_name = str(host_name)
        if 'http://' in host_name or 'https://' in host_name:
            host_name = host_name[host_name.find('://') + 3:]

        print('*' * 60 + '\n')
        print('start scanning website: {}'.format(host_name))

        try:
            server_ip = socket.gethostbyname(host_name)
            print('server ip is: {}'.format(str(server_ip)))

        except socket.error:
            # If the DNS resolution of a website cannot be finished, abort that website.
            print('hostname {} unknown!!!'.format(host_name))
            self.__usage()
            return {}
            # May need to return specific value to indicate the failure.

        start_time = time.time()
        output = self.__scan_ports(server_ip, self.__delay, message.encode('utf-8'))
        stop_time = time.time()

        print('host {} scanned in  {} seconds'.format(host_name, stop_time - start_time))
        print('finished scan!\n')

        return output

    def set_thread_limit(self, limit):
        """
        Set the maximum number of thread for port scanning

        :param limit: the maximum number of thread running concurrently, default to 1000.
        """
        limit = int(limit)

        if limit <= 0 or limit > 50000:
            print(
                'Warning: Invalid thread number limit {}!'
                'Please make sure the thread limit is within the range of (1, 50,000)!'.format(limit)
            )
            print('The scanning process will use default thread limit 1,000.')
            return

        self.__thread_limit = limit

    def set_delay(self, delay):
        """
        Set the time out delay for port scanning in seconds

        :param delay: the time in seconds that a TCP socket waits until timeout, default to 10s.
        """
        delay = int(delay)
        if delay <= 0 or delay > 100:
            print(
                'Warning: Invalid delay value {} seconds!'
                'Please make sure the input delay is within the range of (1, 100)'.format(delay)
            )
            print('The scanning process will use the default delay time 10 seconds.')
            return

        self.__delay = delay

    def show_target_ports(self):
        """
        Print out and return the list of ports being scanned.

        :return: list of ports scanned by current Scanner object.
        :rtype: list
        """
        print ('Current port list is:')
        print (self.target_ports)
        return self.target_ports

    def show_delay(self):
        """
        Print out and return the delay in seconds that a TCP socket waits until timeout.

        :return: timeout interval of the TCP connection in seconds.
        :rtype: int
        """
        print ('Current timeout delay is {} seconds.'.format(self.__delay))
        return self.__delay

    def show_top_k_ports(self, k):
        """
        Print out and return top K commonly used ports. K should be 50, 100 or 1000.

        :param k: top K list will be returned.
        :type k: int
        :return: top K commonly used ports.
        :rtype: list
        """
        port_list = self.check_default_list(k)
        print('Top {} commonly used ports:'.format(k))
        print(port_list)
        return port_list

    def __scan_ports_helper(self, ip, delay, output, message):
        """
        Open multiple threads to perform port scanning

        :param ip: the ip address that is being scanned
        :type ip: str
        :param delay: the time in seconds that a TCP socket waits until timeout
        :type delay: int
        :param output: a dict that stores result in {port, status} style pairs.
        status can be 'OPEN' or 'CLOSE'.
        :type output: dict
        :param message: the message that is going to be included in the scanning packets,
        in order to prevent ethical problem, default to ''.
        :type message: str
        """
        port_index = 0

        while port_index < len(self.target_ports):
            # Ensure the number of concurrently running threads does not exceed the thread limit
            while threading.activeCount() < self.__thread_limit and port_index < len(self.target_ports):
                # Start threads
                thread = threading.Thread(target=self.__TCP_connect,
                                          args=(ip, self.target_ports[port_index], delay, output, message))
                thread.start()
                port_index = port_index + 1

    def __scan_ports(self, ip, delay, message):
        """
        Controller of the __scan_ports_helper() function

        :param ip: the ip address that is being scanned
        :type ip: str
        :param delay: the time in seconds that a TCP socket waits until timeout
        :type delay: int
        :param message: the message that is going to be included in the scanning packets,
        in order to prevent ethical problem, default to ''.
        :type message: str
        :return: a dict that stores result in {port, status} style pairs.
        status can be 'OPEN' or 'CLOSE'.
        """
        output = {}

        thread = threading.Thread(target=self.__scan_ports_helper, args=(ip, delay, output, message))
        thread.start()

        # Wait until all ports being scanned
        while len(output) < len(self.target_ports):
            continue

        # Print opening ports from small to large
        for port in self.target_ports:
            if output[port] == 'OPEN':
                print('{}: {}\n'.format(port, output[port]))

        return output

    def __TCP_connect(self, ip, port_number, delay, output, message):
        """
        Perform status checking for a given port on a given ip address using TCP handshake

        :param ip: the ip address that is being scanned
        :type ip: str
        :param port_number: the port that is going to be checked
        :type port_number: int
        :param delay: the time in seconds that a TCP socket waits until timeout
        :type delay: int
        :param output: a dict that stores result in {port, status} style pairs.
        status can be 'OPEN' or 'CLOSE'.
        :type output: dict
        :param message: the message that is going to be included in the scanning packets,
        in order to prevent ethical problem, default to ''.
        :type message: str
        """
        # Initialize the TCP socket object based on different operating systems.
        # All systems except for 'Windows' will be treated equally.
        curr_os = platform.system()
        if curr_os == 'Windows':
            TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            TCP_sock.settimeout(delay)
        else:
            TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            TCP_sock.settimeout(delay)

        # Initialize a UDP socket to send scanning alert message if there exists an non-empty message
        if message != '':
            UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            UDP_sock.sendto(message, (ip, int(port_number)))

        try:
            result = TCP_sock.connect_ex((ip, int(port_number)))
            if message != '':
                TCP_sock.sendall(message)

            # If the TCP handshake is successful, the port is OPEN. Otherwise it is CLOSE
            if result == 0:
                output[port_number] = 'OPEN'
            else:
                output[port_number] = 'CLOSE'

            TCP_sock.close()

        except socket.error as e:
            # Failed to perform a TCP handshake means the port is probably close.
            output[port_number] = 'CLOSE'
            pass
