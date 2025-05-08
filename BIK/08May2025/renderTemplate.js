/**
replace the value which is in {{}} in template variable from the data object.
*/

function render_template(template, data) {
  return template.replace(/{{\s*(.*?)\s*}}/g, (_, expr) => {
    try {
      const parts = expr.split(".");
      let value = data;
      for (let i = 0; i < parts.length; i++) {
        const part = parts[i];

        if (part === "length") {
          value = value.length.toString();
        } else if (part === "uppercase") {
          value = value.toUpperCase();
        } else if (part === "lowercase") {
          value = value.toLowerCase();
        } else if (part === "first") {
          value = value[0];
        } else if (part === "last") {
          value = value[value.length - 1];
        } else {
          value = value?.[part];
        }
      }
      return value ?? `{{${expr}}}`;
    } catch {
      return `{{${expr}}}`;
    }
  });
}


template1 = "Hi {{name.uppercase}}, you have {{messages.length}} new messages.";
data1 = {
 'name': "John",
 'messages': ["msg1", "msg2"]
};
console.log(render_template(template1, data1))

template2 = "Hello {{person}}, length of number: {{score.length}}";
data2 = {
 'score': 99
};
console.log(render_template(template2, data2))

template3 = "{{title.lowercase}} - First: {{items.first}}, Last: {{items.last}}";
data3 = {
 'title': "TODAY",
 'items': ["apple", "banana", "cherry"]
};
console.log(render_template(template3, data3))
