def render_template(template, data):
    str_list = template.split(" ")
    new_word = ""
    new_data = ""
    op = ''
    # print(str_list)
    for i in range(len(str_list)):
        word = str_list[i]
        if word[0] == '{':
            if str_list[i][-1] != '}':
                op = str_list[i][-1]
                str_list[i] == str_list[:-2]
            if '.' in word:
                new_word = word[2:].split('.')
                new_data = data[new_word[0]]
            if (new_data == None):
                continue
            if 'uppercase' in word:
                str_list[i] = (new_data.upper() + op)
            if 'lowercase' in word:
                str_list[i] = (new_data.lower() + op)
            if 'first' in word:
                str_list[i] = new_data[0]
            if 'last' in word:
                str_list[i] = new_data[0]
            if 'length' in word:
                str_list[i] = str(len(new_data))
    new_template = " ".join(str_list)
    return new_template
    
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