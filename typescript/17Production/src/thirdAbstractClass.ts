// learning abstract class 
// A abstract is totally a blue print no new objects can be formed out of it but new class can 

abstract class TakePhoto{
    constructor(
        public cameraMode: string, 
        public filter: string 
    ){}

    abstract getSepia(): void // it has to be implements later in other class becasue it is abstract method this need to be defiend in the class with extend this abstractg class 

    getReelTime():number{ // this function does not give error as it is not abstract and does not need to be defined in the new class
        // some complex calculation 
        return 8
    }
}  


class Instagram extends TakePhoto{
    constructor(
      public cameraMode: string, 
      public filter: string, 
      public burst: number
    ){
        super(cameraMode, filter)
    }

    getSepia(): void{
        console.log("Sepia")
    }
}
const nobita = new TakePhoto("test", "Test")
const nobita2 = new Instagram("t","t",1)

export{}