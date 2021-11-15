### hextools.py
Checks some known hex file signatures against an input file eg from  https://docs.fileformat.com/image/jpeg/

### inCIDR.py
Checks if an IP address is in a given CIDR block, or if given a single IP, checks if it owned by Google, Microsoft, or Amazon

### extractIP.py
Regex to extract IPV4 addresses from a file in argv[1] and outputs each on a new line

### chrome2data.py
Converts chrome request/response (network devtools) from copied string to a dict. Useful in the REPL

### dictSchema.py
Prints the schema of a nested dict

### flattenList.py
Flattens a nested list

### group.py
Returns count of distinct items in a list

### hashfinder.py
Finds hashes of numbers with given salt

### hextodec.py
Converts hex to dec

### randStrs.py
Returns a random string n characters long



### Examples
Scripts can be chained together to help analyse infrastructure eg  
scriptdump$ dig netflix.com|xargs ./extractIP.py|xargs python3 inCIDR.py  
34.251.179.119 owned by AWS  
52.48.35.66 owned by AWS  
52.214.145.233 owned by AWS  
52.30.238.17 owned by AWS  
52.17.229.109 owned by AWS  
52.211.42.108 owned by AWS  
52.16.43.215 owned by AWS  
52.17.27.129 owned by AWS  
