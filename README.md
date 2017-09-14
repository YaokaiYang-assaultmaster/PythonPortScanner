# Python Port Scanner v0.2

An easy to use Python package that could perform port scanning conveniently.

An output example is showed as following:
![Output Example](https://github.com/YaokaiYang-assaultmaster/PythonPortScanner/blob/master/ExampleGraph/ScanResultExample.png)

## Installation  
1. Use `git clone https://github.com/YaokaiYang-assaultmaster/PythonPortScanner.git` command to clone the repository to your own machine.   
2. There is 2 methods for you to use this module.   
	- One is to put `PortScanner package` in your working directory and import `PortScanner` to your code. In this way you can only use it in your current working directory.  
	- The other is to execute `python setup.py install` in the `PortScanner` package. In this way it will be installed to your python's `site-packages` folder. And after that you can use it globally by `import PortScanner`.   
3. Voilà! You are ready to go!

## Usage  
1. Add `import PortScanner` or `from PortScanner import PortScanner`in your code.  
2. Initialize a new PortScanner object using `scanner = PortScanner.PortScanner()` or `scanner = PortScanner()`. You could also put the list of ports you want to scan (if any) as a python `list` and pass it as the `target_ports` argument to the constructor.  
3. Then call `scanner.scan(host_name)` to perform scan task. 
4. __Note that the total scan time for a single is highly related to the timeout value (delay) set for the Scanner object. Thus for the seek of efficiency, the timeout should not be too long.__

## Documentation 
- Constructor  
`__init__(self, target_ports=None)` takes a list of ports or an int as the argument. If not provided, it will perform scanning task using default ports. If a list is provided, the list will be used as the list of ports being scanned. If a int is provided (this int need to be 50, 100 or 1000), the top 50, 100 or 1000 commonly used ports will be used.     

- Functions  
	1. ` scanner.scan(host_name, message = '')` is the function need to be called to perform port scanning. It takes 2 arguments.   
		- `host_name` is the hostname that is going to be scanned
    	- `message` is the message that is going to be included in the scanning packets sent out. This is provided in order to prevent ethical problem. If not provided, no message will be included in the packets.  
	2.  `scanner.set_thread_limit(limit)` is the function to set the maximum number of threads run concurrently for port scanning. It takes 1 argument.  
		- `limit` is the maximum number of threads allowed. The valid limit range is 1 to 50,000. The default value is 1,000.   
	3.  `scanner.set_delay(delay)` is the function to set the timeout delay for port scanning in seconds. It takes 1 argument. 
		- `delay` the time in seconds that a TCP socket waits until timeout. The valid delay range is 1s to 100s. The default value is 10s.   
	4. `scanner.show_target_ports()` is used to get the list of ports being scanned for current Scanner object.     
	5. `scanner.show_delay()` is used to get current timeout interval in seconds that a TCP socket waits.       
	6. `scanner.show_top_k_ports(k)` is used to get top 50, top 100 or top 1000 port lists. Other k will raise an `ValueError` 

- __An example usage case is showed in `PortScanner/PortScanExample.py`__

## Change logs can be found [here](https://github.com/YaokaiYang-assaultmaster/PythonPortScanner/blob/master/CHANGELOG.md)
