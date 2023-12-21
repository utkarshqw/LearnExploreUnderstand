// narrowing 
 function detect(val: number|string){
    // in ts array is treated as object so how to check for array?
    if(typeof val === "string")
    {
        val.toLocaleLowerCase()
    }
   return val + 3 // Error: Operator '+' cannot be applied to types 'string | number' and 'number'.
 }

 function detect2(val: number |string){
    if(typeof val === "string")
    {
      // if typeof is string we return that's why we are allowed to do return at line 16
      return   val.toLocaleLowerCase() 
    }
    return val + 3
 }


 // narrowing using in operator 

 interface User{
    name: string, 
    email: string
 }
 
 interface Admin{
    name: string, 
    email: string, 
    isAdmin: boolean 
 }

 function isAdmin(account: User | Admin){

  //   return account.isAdmin // this is not allowed as it is not certain that account follow the isAdmin class

  // narrow down to fix the above problem 
  if("isAdmin" in account){
    return account["isAdmin"]
  }
 }

 // instanceof 
 function logValue(x: Date | string) {
    if (x instanceof Date) {
      console.log(x.toUTCString());
                 
  (parameter) x: Date
    } else {
      console.log(x.toUpperCase());
                 
  (parameter) x: string
    }
  }

  // type predicates
   

