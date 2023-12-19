 
 const superHero = [] // [] type not defined so never is alloted by ts type inference 

superHero.push("abc") // Argument of type 'string' is not assignable to parameter of type 'never'.


// defining a empty array 
const superman:[] = []
// defining a number or string array 
const superwomen:number[] = [] // ts allows you to declare variables with a specific type and initialize them with an empty array

superwomen.push("a")

// other syntax of defining
const newHeroes:Array<number> = []
newHeroes.push(1)

type User = {
    name: string, 
    isActive: boolean 
}

const allUser:User[] = []

allUser.push({}) // error because push value does not conform to the type defined

// example of array of array of number 

const mlModel: number[][] = [
    [1,2,3],
    ""
] 
