// ==UserScript==
// @name        LibCrypt
// @namespace   *
// @include    *
// @description Encrypt / Decrypt Image Pixel Data
// @version     1
// @require     https://code.jquery.com/jquery-3.1.1.js
// @grant       none
// ==/UserScript==

/* click the encrypted image to populate the solution text field with the correct answer */

function decryptMorse(morse) {
    codeList = {
      ".-"    : 'A',   "-..."  : 'B',   "-.-."  : 'C',   "-.."   : 'D',
      "."     : 'E',   "..-."  : 'F',   "--."   : 'G',   "...."  : 'H',
      ".."    : 'I',   ".---"  : 'J',   "-.-"   : 'K',   ".-.."  : 'L',
      "--"    : 'M',   "-."    : 'N',   "---"   : 'O',   ".--."  : 'P',
      "--.-"  : 'Q',   ".-."   : 'R',   "..."   : 'S',   "-"     : 'T',
      "..-"   : 'U',   "...-"  : 'V',   ".--"   : 'W',   "-..-"  : 'X',
      "-.--"  : 'Y',   "--.."  : 'Z',   ".----" : '1',   "..---" : '2',
      "...--" : '3',   "....-" : '4',   "....." : '5',   "-...." : '6',
      "--..." : '7',   "---.." : '8',   "----." : '9',   "-----" : '0',
      '/': ' ',
    };
  
    var blocks = morse.split(' ');
    var res = '';
    for(var i = 0; i < blocks.length; i++) {
        var block = blocks[i];
        res += codeList[block];
    }
      console.log('Decoded Morse: ' + morse);
      console.log('Plain Text: ' + res);
      return res;
  }
  
  $(function() {
      $('img').on('click', function(e) {
          if(!this.canvas) {
              this.canvas = $('<canvas />')[0];
              this.canvas.width = this.width;
              this.canvas.height = this.height;
              this.canvas.getContext('2d').drawImage(this, 0, 0, this.width, this.height);
          }
          var count = 0;
          var offset = [];
          for(var h = 0; h < this.canvas.height; h++) {
            for(var w = 0; w < this.canvas.width; w++) {
              pixel = this.canvas.getContext('2d').getImageData(w, h, 1, 1).data;
              var pixel_sum = pixel[0] + pixel[1] + pixel[2] + pixel[3];
              white = 1020;
              if(white === (pixel_sum)) {
                console.log('Count: ' + count);
                offset.push(count);
                count = 1;
              } else {
                  count += 1;
              }
            }
          }
           var m = '';
          for(var i = 0; i < offset.length; i++){
            n = offset[i];
            m += String.fromCharCode(n);
          }
         blocks = m.split(' ');
          var res = '';
          for(var x = 0; x < blocks.length; x++) {
            cipher =  blocks[x];
            console.log('Decode block: ' + cipher);
            if(cipher.length >= 1) {
                res += decryptMorse(cipher);
            }
          }
          console.log(res);
          $('[name="solution"]')[0].value = res;
      });
  });