console.log("typescript is here again") 

// we have set many configuration only the output directory 
// so when we do tsc index.ts the js file in create in src folder but it should be forming in dist/index.js 
// so we use tsc -w

// 18 classes 

class User {
    public email: string // everthing we don't mark is public 
    name: string
    // private will only be accessible withing the 
    // privater can also be written like #
    private readonly city: string = "" // we provided a deafult vlaue to so it will not throw error if we do not write it 
    constructor(email: string, name: string){
        this.email = email; // here we are saying take value from argument and give it to line 10.
        this.name = name // this.name refers to name on line 11

    }
}

// creating an object from the class User 
// const saitama = new User(email: "h@h.com", name: "saitama") wrong way 
const saitama = new User("saitama@anime.com", "saitama")
saitama.city="tokyo"
saitama.city // not allowed to write but is allowed to access 


// other way of writing class 
class User2{
    readonly city: string = "Jaipur"
    constructor(
        public email: string,
        public name: string,
        private userId: string 
        ){}
}

// 19 getters and setters 

class User3 {
    private _courseCount = 1 // we know that it private so it can only be accessed within the class so to use it we make getters and setters 
    readonly city: string= "Jaipur"
    
    // making a variable so that it is available after inheritence 
    // protected
    protected _courseCount2 = 1

    constructor(
        public email: string, 
        public name: string, 

    ){}

   get getAppleEmail(): string {     // get
       return `apple${this.email}`
   }

   get courseCount(): number {
    return this._courseCount
   }
   // no return type in setters 
   set courseCount(courseNum){
    if(courseNum <= 1){
        throw new Error("course count should be more than 1")
    }

    this._courseCount = courseNum 
   }

   // Creating a private method 
   // method can only be used with in the class 
   private deleteToken(){
     console.log("Token deleted")
   }
     
   
}


// making a subuser which has all the properties of class User3
// It cannot acquire the private properties or methods 

class SubUser extends User3 {
    isFamily:boolean = true
    changeCourseCount(){
        this._courseCount = 4
        this._courseCount2 = 4
    }

}