CRC or Cyclic Redundancy Check is a method of detecting accidental changes/errors in the communication channel.

CRC uses Generator Polynomial which is available on both sender and receiver side.
An example generator polynomial is of the form like x3 + x + 1.
This generator polynomial represents key 1011.
Another example is x2 + 1 that represents key 101.

INPUT from the user -> in binary form, provided a space character between each binary digit.
Example 1:

============= CRC =============

Enter The Message Size: 8
Enter The Message: 1 0 0 1 1 1 0 1

Enter The Generator Size: 4
Enter The Generator: 1 0 0 1

============= CRC =============

SENDER
======>
Message: 1 0 0 1 1 1 0 1
Generator: 1 0 0 1
CRC: 1 0 0
Transmitted Codeword: 1 0 0 1 1 1 0 1 1 0 0

NOISY CHANNEL SIMULATION
========================>
Enter the number of Bits to Flip: 1
Enter the Bit position to Flip: 3

RECEIVER
========>
Received Codeword: 1 0 1 1 1 1 0 1 1 0 0
Remainder: 1 0 0

TRANSMISSION ERROR DETECTED!

Example 2:

============= CRC =============

Enter The Message Size: 8
Enter The Message: 1 0 0 1 1 1 0 1

Enter The Generator Size: 4
Enter The Generator: 1 0 0 1

============= CRC =============

SENDER
======>
Message: 1 0 0 1 1 1 0 1
Generator: 1 0 0 1
CRC: 1 0 0
Transmitted Codeword: 1 0 0 1 1 1 0 1 1 0 0

NOISY CHANNEL SIMULATION
========================>
Enter the number of Bits to Flip: 0
Invalid Request! Codeword not changed.

RECEIVER
========>
Received Codeword: 1 0 0 1 1 1 0 1 1 0 0
Remainder: 0 0 0

TRANSMISSION SUCCESSFUL!