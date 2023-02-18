# Error-control Codes
Zhang Zhiwen - Scientic programming, deep learning methods

Category of code:
- Secret codes (cryptography)
- Error control codes
- Source coding (data compression)

## Code
A code is a method to add some additional, redundant information into the original message.

Application: information transmission, data storage

## Example: Phone conversation  
Repetition code:  
Can detect any 1-error (send twice) (1-error: 1 digit is wrong)  
Cannot detect some 2-errors  
Can correct any 1-error (send 3 times)  
Cannot correct some 2-errors

## Definition
Data: original message  
Encoded data/Codeword  
Code rate: ratio between length of original language and length of encoded message (1/3)  
Correction power (all 1-errors)

## General Error Control Scheme
Data -[Encoder]-> Encoded data -[Communication channel]-> (Corrupted) encoded data -[Decoder]-> Detection/Correction

## Basic Principle of Error Control
Adding redundancy to data

## Criteria
Bigger code rate  
Detect/correct more error  
Easier to implement

## Check Digit in HKID Numbers
Format: $X \ n_1\  ... \  n_6 \ (n_7)$  
Convert $X$ into a number  
Mulitply by 8, 7, ..., 2, sum, find remainder 0 - 10(A), subtract

Code rate: 7/8
Can detect all errors occurred in $n_1$ to $n_7$  
Cannot detect some 2-errors  
Cannot correct some 1-errors  
Can detect all 2-errors due to transposition of digits

## ISBN

## Credit Card

## Binary Code
ASCII

### Single-parity-check Code

### Binary Repetition Code
Repeat every digit 3 times  
Can correct 1-errors  
Code rate: 1/3

### Hamming Codes
Can correct all 1-errors at a cost which is less than sending the entire message twice  
Best: Hamming (7, 4) code  
$c_1 = d_1 + d_3 + d_5 + d_7$, $c_2 = d_2 + d_3 + d_6 + d_7$, $c_4 = d_4 + d_5 + d_6 + d_7$  
Convert $c_4c_2c_1$ to decimal  
Code rate: 4/7

### Minimum Distance of Codes
Detection power: $d - 1$ or fewer errors  
Correction power: $\dfrac{d - 1}{2}$ or fewer errors