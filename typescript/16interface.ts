interface User {
  readonly dbId: number,
  email: string,
  userId: number,
  googleId?: string,

  // methods
  // 1 way
  startTrail: () => string,

  // 2 way
  startTrail2(): string,

  // method with string parameter and return value number
  getCoupon(couponname: string,value: number):number 

}

// reopening the interface 
interface User {
    githubToken?: string  // making it optional so that it does not show error
}

// inheritance in interface 
// new inheritance which has all properties of User interface
interface Admin extends User {
 role: "admin" | "ta" | "learner"
}

// >1 interface can be extend
interface NewInterface extends User, Admin{

}

const spongebob: User = {
     dbId: 1, 
     email: "",
     userId: 1,
     startTrail: () => {
        return "string"
     },
     // writing startTrail2 in different way
     startTrail2() {
        return "string"
     },
    //  getCoupon(){ // defined number argument but no error showing 
    //     return 1
    //  },
     getCoupon(name:"u", val: 1){ // can use custom name in argument
        return 1
     }
 };
