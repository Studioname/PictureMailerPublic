This program will send a number of embedded images to an email and send then to every address listed in addresses.txt.
Addresses.txt is imported as a list, which is then iterated over. The program will save the last index it has iterated
over to iterator.txt in case anything goes wrong. The mail send part is wrapped in a try/catch block to prevent errors.
If the user wants to send repeat emails they can uncomment out lines 49 and 50 - If the user only wishes to send a limited
number of them they may leave the lines commented and manually reset the iterator when it has the same value as the number
of addresses in addresses.txt.