"""
replace the value which is in {{}} in template variable from the data object.
"""
import re

def render_template(template, data):
    def resolve(expr):
        parts = expr.split('.')
        value = data
        try:
            for part in parts:
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
                else:
                    value = value.get(part) if isinstance(value, dict) else getattr(value, part, None)
            return str(value)
        except:
            return f"{{{{{expr}}}}}"  # Keep the original if something breaks

    return re.sub(r"{{\s*(.*?)\s*}}", lambda m: resolve(m.group(1)), template)

    
template1 = "Hi {{name.uppercase}}, you have {{messages.length}} new messages.";
data1 = {
 'name': "John",
 'messages': ["msg1", "msg2"]
};
print(render_template(template1, data1))

template2 = "Hello {{person}}, length of number: {{score.length}}";
data2 = {
 'score': 99
};
print(render_template(template2, data2))

template3 = "{{title.lowercase}} - First: {{items.first}}, Last: {{items.last}}";
data3 = {
 'title': "TODAY",
 'items': ["apple", "banana", "cherry"]
};
print(render_template(template3, data3))
