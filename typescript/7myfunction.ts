//  7 // Do you really know functions.
function addTwo(num:number){ // this num agrument can be anything so any is infered to it by ts

    return num + 2 
}

function getUpper(val: string){
    return val.toUpperCase()
}



// more than one parameter
function signUpUser(name: string, email: string, isPaid: boolean){} 

// arrow function 
let loginUser = (name: string, email: string, isPaid: boolean = true) => {}// default value can also be provided 

addTwo(5)
getUpper("utkarsh")
signUpUser("a","b",true)
loginUser("a","b",true) // if one argument is ommited ts gives error 

export {}