1. What is a regular expression and how does it work?
A regular expression is a pattern that can be searched in a way that is similar to a state machine.  Each part is checked, if an input string matches the pattern, it will continue to check the remainder of the string. If it fails, it will go back to the beginning and continue checking the rest of the input.


2. What is an array and how does it work?
An array is a data structure consisting of a collection of elements with unique indices.  These are stored in sequencial memory, so, depending on the programming language used, the size of the array can be automatically assigned, or it will need to be manually assigned and resized as needed. Array elements can be found by by either using the index key, such as "myIndex[0]" or by calculating memory locations.


3. What is a hash table and how does it work?
A hash table is a data structure used to store keys and values using a hash function to compute the index.  These are designed to evenly spread information across an array, and to be able to find information very quickly (in constant time). The way this works is by using a hash function to convert the key element to an integer, and then using a modulo based on array length to calculate where to put the data.