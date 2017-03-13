## Python Port Scanner v0.1

A Python module that could perform port scanning conveniently. 

### Installation  
1. Use `git clone https://github.com/YaokaiYang-assaultmaster/Python-Port-Scanner-Module` command to clone the repository to your own machine.   
2. Put `PortScanner.py` in your working directory or in`/Users/YourName/Library/Python/2.7/lib/python/site-packages`   
3. You are ready to go!

### Usage  
1. Add `import PortScanner` in your code.  
2. Initilize a new PortScanner object using `scanner = PortScanner.PortScanner()`. You could also put the list of ports you want to scan as a `[]` and pass it as argument to the constructor.  
3. Then call `scanner.scan(host_name)` to perform scan task. 

### Documentation 
- Constructor  
`__init__(self, target_ports = None)` takes a list of ports as the argument. If not provided, it will perform scanning task using default ports.   

- Functions  
	1. ` scan(self, host_name, message = '')` is the function need to be called to perform port scanning. It takes 2 arguments.   
		- `host_name` is the hostname that is going to be scanned
    	- `message` is the message that is going to be included in the scanning packets sent out. This is provided in order to prevent ethical problem. If not provided, no message will be included in the packets.  
	2.  `set_thread_limit(self, num)` is the function to set the maximum number of threads run concurrently for port scanning. It takes 1 argument.  
		- `num` is the maximum number of threads allowed.   
	3.  `set_delay(self, delay)` is the function to set the timeout delay for port scanning in seconds. It takes 1 argument. 
		- `delay` the time in seconds that a TCP socket waits until timeout. The valid delay range is 1s to 100s. The default value is 10s.   
	4. `show_target_ports(self)` is used to print out the list of ports being scanned.   
	5. `show_delay(self)` is used to print out the delay in seconds that a TCP socket waits until timeout.   