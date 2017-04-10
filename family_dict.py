# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    'dad': {
        'name': 'Vladimir',
        'age': 65
    },
    'mother': {
        'name': 'Elena',
        'age': 55
    },
    'brother': {
        'name': 'Stas',
        'age': 35
    },
    'husband': {
        'name': 'Matan',
        'age': 28
    },
    'dog': {
        'name': 'Charlie',
        'age': 2
    },
}

# Using a dictionary comprehension, produce output that looks like the following example.
# 'Krista is my sister and is 42 years old'
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)
family_string = {str(v['name'])+' is my '+str(k)+' and is '+str(v['age'])+' years old.' for(k,v) in my_family.items()}
print(family_string)
