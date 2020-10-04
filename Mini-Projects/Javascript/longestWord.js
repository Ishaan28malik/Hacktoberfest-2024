// LANGUAGE: Javascript
// ENV: Node.js
// to run it: node longestWord.js

const longestWord = (string) => {
  var str = string.split(" ");
  var longest = 0;
  var result = null;
  for (var i = 0; i < str.length; i++) {
    if (longest < str[i].length) {
      longest = str[i].length;
      result = str[i];
    } else if (longest == str[i].length) {
      result = result + " " + "and" + " " + str[i];
    }
  }
  return result;
};

console.log(longestWord("She Sells Seashells by the Seashore"));
