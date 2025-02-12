# Basic Match and Search
import re

# Match if the string starts with 'Hello'
pattern = "^Hello"
string = "Hello World"
match = re.match(pattern, string)

if match:
    print("Match found:", match.group())  # Output: Match found: Hello
else:
    print("No match found")

# Search for a substring anywhere in the string
pattern = "World"
search = re.search(pattern, string)

if search:
    print("Search found:", search.group())  # Output: Search found: World
else:
    print("No match found")

# ------------------------------------------------------------------------------------------------------------

 # Find All Matches
import re

pattern = r"\d+"  # Match one or more digits
string = "There are 12 apples, 30 bananas, and 45 cherries."

matches = re.findall(pattern, string)
print("Found numbers:", matches)  # Output: Found numbers: ['12', '30', '45']

# --------------------------------------------------------------------------------------------------------------
# Using Groups for Subpatterns
import re

pattern = r"(\d+)\s+(\w+)"  # Match a number followed by a word
string = "123 apples, 456 bananas"

matches = re.findall(pattern, string)
print("Found matches:", matches)  # Output: Found matches: [('123', 'apples'), ('456', 'bananas')]

# -----------------------------------------------------------------------------------------------------------------
# Replace Text Using sub
import re

pattern = r"\d+"  # Match all numbers
string = "There are 12 apples, 30 bananas, and 45 cherries."

# Replace all numbers with '#'
new_string = re.sub(pattern, "#", string)
print("Updated string:", new_string)  # Output: There are # apples, # bananas, and # cherries.

# --------------------------------------------------------------------------------------------------------------

# Split a String Using split
import re

pattern = r"\s+"  # Match one or more spaces
string = "This is   a test string"

# Split the string at spaces
words = re.split(pattern, string)
print("Words:", words)  # Output: Words: ['This', 'is', 'a', 'test', 'string']

# --------------------------------------------------------------------------------------------------------------

