import sys
import subprocess
import socket
import threading
import time

class PortScanner:

    # default ports to be scanned
    __port_list = [1,3,6,9,13,17,19,20,21,22,23,24,25,30,32,37,42,49,53,70,79,80,81,82,83,84,88,89,99,106,109,110,113,119,125,135,139,143,146,161,163,179,199,211,222,254,255,259,264,280,301,306,311,340,366,389,406,416,425,427,443,444,458,464,481,497,500,512,513,514,524,541,543,544,548,554,563,587,593,616,625,631,636,646,648,666,667,683,687,691,700,705,711,714,720,722,726,749,765,777,783,787,800,808,843,873,880,888,898,900,901,902,911,981,987,990,992,995,999,1000,1001,1007,1009,1010,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1102,1104,1105,1106,1107,1110,1111,1112,1113,1117,1119,1121,1122,1123,1126,1130,1131,1137,1141,1145,1147,1148,1151,1154,1163,1164,1165,1169,1174,1183,1185,1186,1192,1198,1201,1213,1216,1217,1233,1236,1244,1247,1259,1271,1277,1287,1296,1300,1309,1310,1322,1328,1334,1352,1417,1433,1443,1455,1461,1494,1500,1503,1521,1524,1533,1556,1580,1583,1594,1600,1641,1658,1666,1687,1700,1717,1718,1719,1720,1723,1755,1761,1782,1801,1805,1812,1839,1862,1863,1875,1900,1914,1935,1947,1971,1974,1984,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2013,2020,2021,2030,2033,2034,2038,2040,2041,2042,2045,2046,2047,2048,2065,2068,2099,2103,2105,2106,2111,2119,2121,2126,2135,2144,2160,2170,2179,2190,2196,2200,2222,2251,2260,2288,2301,2323,2366,2381,2382,2393,2399,2401,2492,2500,2522,2525,2557,2601,2604,2607,2638,2701,2710,2717,2725,2800,2809,2811,2869,2875,2909,2920,2967,2998,3000,3003,3005,3006,3011,3013,3017,3030,3052,3071,3077,3128,3168,3211,3221,3260,3268,3283,3300,3306,3322,3323,3324,3333,3351,3367,3369,3370,3371,3389,3404,3476,3493,3517,3527,3546,3551,3580,3659,3689,3703,3737,3766,3784,3800,3809,3814,3826,3827,3851,3869,3871,3878,3880,3889,3905,3914,3918,3920,3945,3971,3986,3995,3998,4000,4001,4002,4003,4004,4005,4045,4111,4125,4129,4224,4242,4279,4321,4343,4443,4444,4445,4449,4550,4567,4662,4848,4899,4998,5000,5001,5002,5003,5009,5030,5033,5050,5054,5060,5080,5087,5100,5101,5120,5190,5200,5214,5221,5225,5269,5280,5298,5357,5405,5414,5431,5440,5500,5510,5544,5550,5555,5560,5566,5631,5633,5666,5678,5718,5730,5800,5801,5810,5815,5822,5825,5850,5859,5862,5877,5900,5901,5902,5903,5906,5910,5915,5922,5925,5950,5952,5959,5960,5961,5962,5987,5988,5998,5999,6000,6001,6002,6003,6004,6005,6006,6009,6025,6059,6100,6106,6112,6123,6129,6156,6346,6389,6502,6510,6543,6547,6565,6566,6580,6646,6666,6667,6668,6689,6692,6699,6779,6788,6792,6839,6881,6901,6969,7000,7001,7004,7007,7019,7025,7070,7100,7103,7106,7200,7402,7435,7443,7496,7512,7625,7627,7676,7741,7777,7800,7911,7920,7937,7999,8000,8001,8007,8008,8009,8010,8021,8031,8042,8045,8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,8093,8099,8180,8192,8193,8200,8222,8254,8290,8291,8300,8333,8383,8400,8402,8443,8500,8600,8649,8651,8654,8701,8800,8873,8888,8899,8994,9000,9001,9002,9009,9010,9040,9050,9071,9080,9090,9099,9100,9101,9102,9110,9200,9207,9220,9290,9415,9418,9485,9500,9502,9535,9575,9593,9594,9618,9666,9876,9877,9898,9900,9917,9929,9943,9968,9998,9999,10000,10001,10002,10003,10009,10012,10024,10082,10180,10215,10243,10566,10616,10621,10626,10628,10778,11110,11967,12000,12174,12265,12345,13456,13722,13782,14000,14238,14441,15000,15002,15003,15660,15742,16000,16012,16016,16018,16080,16113,16992,17877,17988,18040,18101,18988,19101,19283,19315,19350,19780,19801,19842,20000,20005,20031,20221,20828,21571,22939,23502,24444,24800,25734,26214,27000,27352,27355,27715,28201,30000,30718,30951,31038,31337,32768,32769,32770,32771,32772,32773,32774,32775,32776,32777,32778,32779,32780,32781,32782,32783,32784,33354,33899,34571,34572,35500,38292,40193,40911,41511,42510,44176,44442,44501,45100,48080,49152,49153,49154,49155,49156,49157,49158,49159,49160,49163,49165,49167,49175,49400,49999,50000,50001,50002,50006,50300,50389,50500,50636,50800,51103,51493,52673,52822,52848,52869,54045,54328,55055,55555,55600,56737,57294,57797,58080,60020,60443,61532,61900,62078,63331,64623,64680,65000,65129,65389]
    __thread_limit = 1000
    __delay = 10
    

    """
    Constructor of a PortScanner object

    Keyword arguments:
    target_ports -- the list of ports that is going to be scanned (default self.__port_list)
    """
    def __init__(self, target_ports = None):
        # If target ports not given in the arguments, use default ports
        # If target ports is given in the arguments, use given port lists
        if target_ports is None:
            self.target_ports = self.__port_list
        else:
            self.target_ports = target_ports


    """
    Return the usage information for invalid input host name. 
    """
    def __usage(self):
        print('python Port Scanner v0.1')
        print('please make sure the input host name is in the form of "something.com" or "http://something.com!"\n')


    """
    This is the function need to be called to perform port scanning

    Keyword arguments:
    host_name -- the hostname that is going to be scanned
    message -- the message that is going to be included in the scanning packets, in order to prevent
        ethical problem (default: '')
    """
    def scan(self, host_name, message = ''):

        if 'http://' in host_name or 'https://' in host_name:
            host_name = host_name[host_name.find('://') + 3 : ]

        print('*' * 60 + '\n')
        print('start scanning website: ' + str(host_name))

        try:
            server_ip = socket.gethostbyname(str(host_name))
            print('server ip is: ' + str(server_ip))

        except socket.error as e:
            # If the DNS resolution of a website cannot be finished, abort that website.

            #print(e)
            print('hostname %s unknown!!!' % host_name)

            self.__usage()

            return {}

            # May need to return specificed values to the DB in the future

        start_time = time.time()
        output = self.__scan_ports(server_ip, self.__delay, message)
        stop_time = time.time()

        print('host %s scanned in  %f seconds' %(host_name, stop_time - start_time))

        print('finish scanning!\n')

        return output


    """
    Set the maximum number of thread for port scanning

    Keyword argument:
    num -- the maximum number of thread running concurrently (default 1000)
    """
    def set_thread_limit(self, num):
        num = int(num)

        if num <= 0 or num > 50000:

            print('Warning: Invalid thread number limit! Please make sure the thread limit is within the range of (1, 50,000)!')
            print('The scanning process will use default thread limit!')

            return

        self.__thread_limit = num


    """
    Set the time out delay for port scanning in seconds

    Keyword argument:
    delay -- the time in seconds that a TCP socket waits until timeout (default 10)
    """
    def set_delay(self, delay):

        delay = int(delay)
        if delay <= 0 or delay > 100:

            print('Warning: Invalid delay value! Please make sure the input delay is within the range of (1, 100)')
            print('The scanning process will use the default delay time')

            return 

        self.__delay = delay


    """
    Print out the list of ports being scanned
    """
    def show_target_ports(self):
        print ('Current port list is:')
        print (self.target_ports)


    """
    Print out the delay in seconds that a TCP socket waits until timeout
    """
    def show_delay(self):
        print ('Current timeout delay is :%d' %(int(self.__delay)))


    """
    Open multiple threads to perform port scanning

    Keyword arguments:
    ip -- the ip address that is being scanned
    delay -- the time in seconds that a TCP socket waits until timeout
    output -- a dict() that stores result pairs in {port, status} style (status = 'OPEN' or 'CLOSE')
    message -- the message that is going to be included in the scanning packets, in order to prevent
        ethical problem (default: '')
    """
    def __scan_ports_helper(self, ip, delay, output, message):

        '''
        Multithreading port scanning
        '''

        port_index = 0

        while port_index < len(self.target_ports):

            # Ensure that the number of cocurrently running threads does not exceed the thread limit
            while threading.activeCount() < self.__thread_limit and port_index < len(self.target_ports):

                # Start threads
                thread = threading.Thread(target = self.__TCP_connect, args = (ip, self.target_ports[port_index], delay, output, message))
                thread.start()
                port_index = port_index + 1


    """
    Controller of the __scan_ports_helper() function

    Keyword arguments:
    ip -- the ip address that is being scanned
    delay -- the time in seconds that a TCP socket waits until timeout
    message -- the message that is going to be included in the scanning packets, in order to prevent
        ethical problem (default: '')
    """        
    def __scan_ports(self, ip, delay, message):

        output = {}

        thread = threading.Thread(target = self.__scan_ports_helper, args = (ip, delay, output, message))
        thread.start()

        # Wait until all port scanning threads finished
        while (len(output) < len(self.target_ports)):
            continue

        # Print openning ports from small to large
        for port in self.target_ports:
            if output[port] == 'OPEN':
                print(str(port) + ': ' + output[port] + '\n')

        return output
        # May need to add codes for storing results to database here



    """
    Perform status checking for a given port on a given ip address using TCP handshake

    Keyword arguments:
    ip -- the ip address that is being scanned
    port_number -- the port that is going to be checked
    delay -- the time in seconds that a TCP socket waits until timeout
    output -- a dict() that stores result pairs in {port, status} style (status = 'OPEN' or 'CLOSE')
    message -- the message that is going to be included in the scanning packets, in order to prevent
        ethical problem (default: '')
    """
    def __TCP_connect(self, ip, port_number, delay, output, message):
        # Initilize the TCP socket object
        TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        TCP_sock.settimeout(delay)


        # Initilize a UDP socket to send scanning alart message
        if message != '':
            UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            UDP_sock.sendto(str(message), (ip, int(port_number)))

        try:
            result = TCP_sock.connect_ex((ip, int(port_number)))
            if message != '':
                TCP_sock.sendall(str(message))
            
            # If the TCP handshake is successful, the port is 'OPEN'. Otherwise it is CLOSE
            if result == 0:
                output[port_number] = 'OPEN'
            else:
                output[port_number] = 'CLOSE'

            TCP_sock.close()

        except socket.error as e:

            output[port_number] = 'CLOSE'
            #print(e)
            pass


