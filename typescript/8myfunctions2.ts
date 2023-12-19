// 8 // A better way to write function

 // {after () define :type of return value 
function addTwo(num:number):number{

    return num + 5
}

// return type in arrow function 
//A function whose declared type is neither 'undefined', 'void', nor 'any' must return a value.
// function getHello = (s: string):string => {}

const getHello2 = (s: string): string => {return "a"}

const heroes = ["a", "b",1] 


//(method) Array<string>.map<string>(callbackfn: (value: string, index: number, array: string[]) => string, thisArg?: any): string[]

// ts infered the value of hero below
heroes.map(hero=>{
    return `hero is ${hero}`
})

// type should be alloted in case of map 
heroes.map((hero):string=>{
    return  `hero is ${hero}`}
)

// if a function in not returning anything use type void
function consoleError(errmsg:string): void{
    console.log(errmsg)
}

function handleError(errmsg:string):never{
    throw new Error(errmsg);
}