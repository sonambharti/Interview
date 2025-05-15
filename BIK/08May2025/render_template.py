"""
replace the value which is in {{}} in template variable from the data object.
"""

import re 

def resolve(expr, data):
    parts = expr.split('.') if '.' in expr else expr
    part = parts[1] if len(parts)==2 else None
    # print(part)
    value = ""
    if '.' in expr:
        value = data[parts[0]]
    else:
        if parts in data:
            value = data[parts]
        else: 
            return f'{{{{{expr}}}}}'
    
    if part == "length":
        value = len(value)
    elif part == "uppercase":
        value = value.upper()
    elif part == "lowercase":
        value = value.lower()
    elif part == "first":
        value = value[0]
    elif part == "last":
        value = value[-1]
    # else:
    #     value = value.get(part) if isinstance(value, dict) else getattr(value, part, None)
    return str(value)
    
def render_template(template, data):
    # pattern = r'\{\{\w+\.\w*\}\}' # this will include the braces in the words
    pattern = r'{{\s*(.*?)\s*}}' # this will exclude the braces
    # newTemplate = re.findall(pattern, template)
    return re.sub(pattern, lambda m: resolve(m.group(1), data), template) # replace the pattern with middle argument from the template
    
    
template1 = "Hi {{name.uppercase}}, you have {{messages.length}} new messages.";
data1 = {
 'name': "John",
 'messages': ["msg1", "msg2"]
};
print(render_template(template1, data1))

template2 = "Hello {{person}}, length of number: {{score.length}}";
data2 = {
 'score': [99]
};
print(render_template(template2, data2))

template3 = "{{title.lowercase}} - First: {{items.first}}, Last: {{items.last}}";
data3 = {
 'title': "TODAY",
 'items': ["apple", "banana", "cherry"]
};
print(render_template(template3, data3))
