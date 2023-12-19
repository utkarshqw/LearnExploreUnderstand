let greet: string = "Hello world"

// greet. it shows all the methods of string becasue we have declared greet as a string 
console.log(greet)
// String variable cannot be assigned a different type value
// greet = true
// This gets rid of error "Cannot redeclare block-scoped variable 'greet'."

// Number
let userId:number= 334455
// userId. // only method related to number will be fetched as the defined variable is number 
userId.toFixed() // even if we don't use number type we will get the type number as it is too obvious/ type inference 

// boolean 
let isLoggedIn: boolean = false 

// something are too obvious so don't overuse typescript 

// type "any"
// ts has no idea what to infer the variable hero 
// let hero;

// function getHero(){
//     return "thor"  // here i can return anything stirng,boolean, number
// }

// hero = getHero()

let hero:string ;
function getHero(){
    return true
}
hero = getHero() // error because hero expects string as value

export {}