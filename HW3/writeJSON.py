"""
Using the factorial() function form a dictionary,
where keys are integers from 1 to 20 and values are their factorials.

Write the dictionary to a text file using indented json.dumps().
"""
import json

def factorial(number) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)

dec_factorial = {}
for i in range(1, 20):
    dec_factorial[i]=factorial(i)

#print (dec_factorial)
output_json_string = json.dumps(dec_factorial,indent=4)
print(output_json_string)
with open('lesson_3.json', 'w') as f:
    f.write(output_json_string)
