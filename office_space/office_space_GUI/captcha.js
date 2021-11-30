//https://www.makeuseof.com/captcha-validation-html-css-javascript/


let captcha_components = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",

     "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
     "!", "@", "#", "$", "%", "&", "^",]

let current_captcha = []



for (let i = 1; i <= 9; i++) {
    current_captcha.push(captcha_components[Math.floor(Math.random() * captcha_components.length)])
} 

let captcha_validator = current_captcha.join("")

console.log(current_captcha)
console.log(captcha_validator)

document.getElementById("#captcha")
captcha.style.color= "#f7f7f1"
captcha.innerHTML= captcha_validator

//add event listener for login button --> window.location.href="./assignment_roster.html"
//if (user_role !== ADMIN) {
    //let trash = document.getElementById("remove_seat")
    //trash.style.display= "none"
//}

// let captchaSubmit= document.getElementById("").addEventListener(click, "captcha_selection")
//  
// function captcha_selection () {
//     
// }
// )