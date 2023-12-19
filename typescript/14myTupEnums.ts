// Tuples 

// using tuples for array with element in certain order 
let tUser:[string, number, boolean]
tUser = ["hc", 131, true ] 

let rgb:[number, number, number] = [255, 123, 112]

// user of type [number and string]
type User = [number, string]
const newUser:User = [112, "example@google.com"]
// problem with tuple not showing error while we are assigning index 0 a string which should be a number 
newUser[1] = "abc"
newUser.push("a")
newUser.push(false)


