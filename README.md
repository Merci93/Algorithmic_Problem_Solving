# Daily Algorithmic challenges and solutions.
### **Day 1**
Given an array of integers, find the sum of its elements. Test array=[2,3,4,5,6].

### **Day 2**
Two students Alice and Bob submitted a school project. Their lecturer rates the two projects, awarding points on a
scale from 1 to 100 for three categories: problem clarity, originality, and difficulty. The rating for Alice's
challenge are: a = (a[0], a[1], a[2]), and the rating for Bob's challenge are b = (b[0], b[1], b[2]). Your task is to
find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

- If **a[i] > b[i]**, then Alice is awarded 1 point.
- If **a[i] < b[i]**, then Bob is awarded 1 point.
- If **a[i] = b[i]**, then neither person receives a point.

Comparison points is the total points a person earned. Given a and b, determine their respective comparison points.

Example:\
a = [1, 2, 3]\
b = [3, 2, 1]\
For elements **0**, Bob is awarded a point.\
For elements **1**, no points are earned.\
Finally, for elements **2**, Alice receives a point.\
The return array is [1, 1] with Alice's score first and Bob's second.

### **Day 3**: 
Write a function to check and return True if the second argument (string) starts with the same letter(s) (1 or 2) as
the ending of the first argument (string)\
Example:\
strCheck('abc', 'bc') returns true\
strCheck('abc', 'd') returns false\
strCheck(a,b) :- a and b are strings, if the last strings of 'a' are exactly 'b' then true else false

### **Day 4**:
Given a string of words, return the length of the shortest word(s). String will never be empty and you do not need to
account for different data types.\
e.g words=['collar', 'kola', 'umbrella', 'yemi']\
shortest strings are 'kola' 'yemi' and length is 3

### **Day 5**:
Create a function that takes the age in years and returns the age in days.

### **Day 6**:
Write a function that calculates the factorial of a non-negative integer n.

### **Day 7-8**:
Write a function that checks whether a given string is a palindrome. A palindrome is a word, phrase, number, or other
sequences of characters that reads the same forward and backward. For example, "racecar" is a palindrome.

### **Day 9**:
Write a function that takes a string as input and returns the string reversed.
