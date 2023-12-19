// Using interface to decide things that must be there in a class

interface TakePhoto{
    cameraMode: string 
    filter: string
    burst: number 
}
interface Story{
    createStory(): void 
}
// use of implements in class 
class Instagram implements TakePhoto {
    constructor(
        public cameraMode: string,
        public filter: string,
        public burst: number 
        
    ){}
}

class Youtube implements TakePhoto, Story {
    constructor(
        public cameraMode: string,
        public filter: string,
        public burst: number,
        public short: string // we have not defined the typ eshort but it is allowed as more fileds can be added but not less 

        
    ){}

    // Depite of provideing Story interface here we still ne the write the method here 
    // If there is mistake in spelling ts shows error
    createStory():void {
        console.log("story")
    }
}