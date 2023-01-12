This program will embed images to an email and send then to every address listed in addresses.txt.
Addresses.txt is imported as a list, which is then iterated over. The program will save the last index it has iterated
over to iterator.txt in case anything goes wrong. The mail send part is wrapped in a try/catch block to prevent errors.
If the user wants to send repeat emails they can uncomment out lines 49 and 50 - If the user only wishes to send a
limited number of them they may leave the lines commented and manually reset the iterator when it has the same value as
the number of addresses in addresses.txt.

Credit due to Rio at https://stackoverflow.com/users/8230132/rio for his answer https://stackoverflow.com/a/52329759
on which the program is based.

Todo: Add pictures to a list and iterate through them to embed as opposed to adding them manually
