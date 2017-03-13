import PortScanner as ps

def main():

    scanner = ps.PortScanner()

    website = 'google.com'

    message = 'put whatever message you want here'

    '''
    output contains a dictionary of [port:status] pairs
    in which port is the list of ports we scanned 
    and status is either 'OPEN' or 'CLOSE'
    ''' 
    output = scanner.scan(host_name, message)



if __name__ == "__main__":
    main()