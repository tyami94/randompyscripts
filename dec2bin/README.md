# dec2bin
A decimal to binary converter that is designed to be as small as possible without using any libraries. Can convert HUGE numbers. (Hypothetically, it can handle any length. It's only real limit is 'sys.maxsize', due to lists having a maximum possible length. The most I tested is ((2^131072)-1) (a 131072-bit unsigned integer), which is 39457 digits long. It took a VERY long time to convert. I guess it could be modified to support signed int, but this is more of a proof of concept. I'm probably not going to bother adding support for signed integers.

Files:
  dec2bin.py: The original dec2bin converter.
  dec2bincomment.py: Standalone dec2bin
    
Variables:
  i = Input Decimal
  a[v] = Output Array
  v = Binary Length of Number
