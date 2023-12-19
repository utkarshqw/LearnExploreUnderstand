type User = {
    name: string;
    email:string;
    isActive: boolean
}

// function parameter of type user and return object of type user
function createUser(user: User): User{
    return {
        name:"", email:"", isActive:true
    }
}
  
export {}