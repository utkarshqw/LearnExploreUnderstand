// readonly keyword is discussed here
// ? optional

type User = {
    readonly _id: string, 
    name: string,
    email: string,
    isActive: boolean 
    ceditCard?:number // this key is optional 
}

let myUser:User = {
    _id: "",
    name: "",
    email: "",
    isActive: true 
}

// myUser._id = "abc" // Cannot assign to '_id' because it is a read-only property.

// combining different types 

type cardNumber = {
    cardnumber: string 
}
type cardDate = {
    cardDate: string 
}

// creating a new type by combining the previous two types and a new one 
type cardDetails = cardNumber & cardDate & {
    cvv: number 
}

export {}