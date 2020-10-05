// LANGUAGE: Javascript
// ENV: Node.js
// to run it: node longestWord.js

function longestWord(str) {
  var string = str.split(" ");
  var longest = 0;
  var result = null;
  for (var i = 0; i < string.length; i++) {
    if (longest < string[i].length) {
      longest = string[i].length;
      result = string[i];
    } else if (longest == string[i].length) {
      result = result + " " + "and" + " " + string[i];
    }
  }
  return result;
}

console.log(longestWord("Pro in Hacktoberfest2020"));
