# dec2bin
A decimal to binary converter that is designed to be as small as possible without using any libraries. (math is imported in the standalone version, but that is only to allow functions like 'math.log' in the expression input. It is not in the standard version.) It can convert HUGE numbers. (Hypothetically, it can handle any length. It's only real limit is 'sys.maxsize', due to lists having a maximum possible length. The most I tested is (2^(2^17))-1 (effectively a 131072-bit unsigned integer), which is 39457 digits long. It took a VERY long time to convert. I guess it could be modified to support signed int, but this is more of a proof of concept. I'm probably not going to bother adding support for signed integers. 

WARNING: Be careful when using incredibly large numbers >\~(2^(2^16))-1. With very large numbers this script can use in excess of 4GB of RAM, and can easily max out part of your CPU. You will not be able to CTRL+C. Anything below (2^(2^10))-1 should play nice on a decent system. Also, IDLE has an INCREDIBLY SLOW implementation of print(). The verbose version will hang IDLE at input values >(2^(2^32))-1. It will also take a very long time on inputs >=\~(2^(2^16))-1

## Files:
  dec2bin.py: The original dec2bin converter.
  
  dec2binstandalone.py: Standalone dec2bin. Not verbose, only returns converted number.
  
  dec2binverbose.py: Standalone dec2bin with verbosity. This code is pretty much impossible to comment due to it's highly esoteric nature, so this explains what is happening as it happens.
  
  16384bittest.txt: contains a 16384-bit integer that acts as an integrity check. This should return a perfectly alternating pattern of 0xAh(1010b). This verifies that working values are not being truncated, because if the working values were truncated, the pattern would not repeat. It would just become psuedo-random.
    
## Variables:

  i = Input Decimal
  
  a\[v\] = Output Array
  
  v = Binary Length of Number
