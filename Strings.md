What are Strings?

- Strings are sequences of characters used to represent textual data in Python.

- They are enclosed within quotation marks (either single ' or double ").

Examples:

Python
"Hello, world!"
'This is a string'

Key Characteristics:

- Immutable: Once created, strings cannot be modified. To change a string, you must create a new one.
- Indexing: Characters in a string are accessed using their index, starting from 0.
- string[index] returns the character at the specified index.
- Negative indices access characters from the end, with -1 being the last character.
- Slicing: Extract substrings using slicing:
string[start:end] returns the substring from start (inclusive) to end (exclusive).
- Omit start to start from the beginning.
- Omit end to go to the end.
- Negative indices can be used for slicing as well.
 - Concatenation: Combine strings using the + operator.
- Repetition: Repeat a string using the * operator.
- Membership Testing: Check if a substring exists within a string using the in keyword.
- String Methods: Python provides numerous built-in methods to manipulate strings, such as:
- len(string): Returns the length of the string.
- string.upper(): Converts the string to uppercase.
- string.lower(): Converts the string to lowercase.
- string.capitalize(): Capitalizes the first character of the string.   
- string.strip(): Removes leading and trailing whitespace.
- string.replace(old, new): Replaces all occurrences of old with new.
- string.split(separator): Splits the string into a list of substrings based on the separator.
- string.join(list): Joins the elements of a list into a string using the string as the separator.

