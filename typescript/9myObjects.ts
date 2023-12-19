// Bad behaviour of objects 9 
function createUser({name:string, isPaid: boolean}){}

createUser({name:"a", isPaid: false})

// function saying it will return object
function createCourse():{}{
    return {}
}

// function saying it will return a object with somekeys 
function createCourse2():{name: string, price: number}{
 return {name:"a",price:2}
}

// calling the function createUser with a extra argument which is not defined earlier
// It would give error but If I define a object with extra argument and then pass it to the function it will not 
createUser({name:"a", isPaid: true, email: "abc@gmail.com"})

let argObj = {name:"a", isPaid: true, email: "abc@gmail.com"}
createUser(argObj) // user extras argument but still not showing error 


export{}
