//https://www.makeuseof.com/captcha-validation-html-css-javascript/


let captcha_components = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",

     "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
     "!", "@", "#", "$", "%", "&", "^",]

let current_captcha = []

// function captcha_selection () {
//     Math.random(Math.floor) * 8) + 1 
// }

for (let i = 1; i <= 9; i++) {
    current_captcha.push(captcha_components[Math.floor(Math.random() * captcha_components.length)])
} 

let captcha_validator = current_captcha.join("")

console.log(current_captcha)
console.log(captcha_validator)

