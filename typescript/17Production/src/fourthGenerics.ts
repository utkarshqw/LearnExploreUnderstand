// Example of generics 
const score: Array<number> = []
const names: Array<string> = [] 

// generics are already provided by ts 

function indentityOne(val: boolean  | number): boolean | number{
    return val 
}

// we do not know what type of data woud be return 
// like nothing is fix
function indentityTwo(val:any):any{
    return val 
}

// here if Type if string string would be returned and same in case of other Types 
function identityThree<Type>(val:Type):Type{ // but one problem suppose the type is number and we have to console .length it's can't be done 
    return val
}

// generic usage in different type here we know if the val is string the return value automatically becomes string
identityThree(3) 
identityThree("a")

 // shortcut 
 function identityThree2<T>(val:T):T{
    return val
}

interface Bootle {
    brand: string, 
    type: number
}

// if user custom made type or interface use the follwing syntax
identityThree2<Bootle>({}) 


// GENERIC IS ARRAY AND ARROW FUNCTION 
function getSearchProducts<T>(products: T[]):T{
    // return 3
    return products[3]
}
// Here , is put after <T,> to show that it's a generic and not a html tag
const getMoreSearchProducts = <T,>(products: T[]): T => {
     const myIndex = 4
     return products[myIndex]
}


// GENERIC CLASSES 
 interface Database{
    connection: string, 
    username: string, 
    password: string
 }

function anotherFunction<T, U extends number>(valOne:T, valTwo:U):object{
    return {
      valOne, 
      valTwo
    }
}

function anotherFunction2<T, U extends Database>(valOne:T, valTwo:U):object{
    return {
      valOne, 
      valTwo
    }
}
anotherFunction(3,"4") // error becaue type U extends number 
anotherFunction2(3,
    {
        connection: "string", 
    username: "string", 
    password: "string" 
    })



interface Quiz{
    name: string, 
    type: string
}    

interface Course{
    name: string, 
    author: string, 
    subject: string
}

class Sellable<T>{
   public cart: T[] = []

   addToCart(product: T){
    this.cart.push(product)
   }
}
