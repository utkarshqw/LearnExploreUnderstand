"use strict";
// Using interface to decide things that must be there in a class
// use of implements in class 
class Instagram {
    constructor(cameraMode, filter, burst) {
        this.cameraMode = cameraMode;
        this.filter = filter;
        this.burst = burst;
    }
}
class Youtube {
    constructor(cameraMode, filter, burst, short // we have not defined the typ eshort but it is allowed as more fileds can be added but not less 
    ) {
        this.cameraMode = cameraMode;
        this.filter = filter;
        this.burst = burst;
        this.short = short;
    }
    // Depite of provideing Story interface here we still ne the write the method here 
    // If there is mistake in spelling ts shows error
    createStory() {
        console.log("story");
    }
}
