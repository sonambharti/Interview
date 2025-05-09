function renderTemplate(template, data) {
  let strList = template.split(" ");
  let newWord = "";
  let newData = "";
  let op = '';

  for (let i = 0; i < strList.length; i++) {
    let word = strList[i];

    if (word[0] === '{') {
      if (word[word.length - 1] !== '}') {
        op = word[word.length - 1];
        word = word.slice(0, -1); // remove punctuation
      }

      if (word.includes('.')) {
        // remove opening {{
        newWord = word.replace("{{", "").replace("}}", "").split('.');
        newData = data[newWord[0]];
      }

      if (newData === undefined || newData === null) {
        continue;
      }

      if (word.includes("uppercase")) {
        strList[i] = newData.toUpperCase() + op;
      }
      if (word.includes("lowercase")) {
        strList[i] = newData.toLowerCase() + op;
      }
      if (word.includes("first")) {
        strList[i] = newData[0];
      }
      if (word.includes("last")) {
        strList[i] = newData[newData.length - 1];
      }
      if (word.includes("length")) {
        strList[i] = newData.length.toString();
      }
    }
  }

  return strList.join(" ");
}

// Test case 1
let template1 = "Hi {{name.uppercase}}, you have {{messages.length}} new messages.";
let data1 = {
  name: "John",
  messages: ["msg1", "msg2"]
};
console.log(renderTemplate(template1, data1));

// Test case 2
let template2 = "Hello {{person}}, length of number: {{score.length}}";
let data2 = {
  score: [99]
};
console.log(renderTemplate(template2, data2));

// Test case 3
let template3 = "{{title.lowercase}} - First: {{items.first}}, Last: {{items.last}}";
let data3 = {
  title: "TODAY",
  items: ["apple", "banana", "cherry"]
};
console.log(renderTemplate(template3, data3));
