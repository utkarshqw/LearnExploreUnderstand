// use union when we are not sure of the type 

let score: number | string = 33 

score = 44
score = "s"

// can also be a group of types 

type User = {
    name: string 
    id: number 
}
type Admin = {
    username: string 
    id: number 
}

let pikachu : User | Admin = {
    name: "a", id: 334
} 

pikachu = {username: "a",id:334}

// multiple types in function parameter 
function getDbId(id:number | string)
{
    console.log(`DB id is ${id}`)
} 
// can use both string or number
getDbId(3)
getDbId("3")

// function which has type "number | string" can't do .toUpperCase()
function uppderCaseError(id:number | string){
id = id.toUpperCase() // Error: Property 'toUpperCase' does not exist on type 'string | number'.
}

// to avoid use typeOf
function upperCaseSolved(id:number | string){
    if(typeof id === "string") 
    {
        id.toLowerCase()
    }
}

// Array which can have both string and number 
// wrap (string | number) for things to work  
const data: (string | number) [] = ["1", 2]

// not only types but suppose if we can say that a thing can only be alloted three value

let coin:5|10|20
coin = 10
coin = 100 // Error: Type '100' is not assignable to type '5 | 10 | 20'.










