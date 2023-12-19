// if we use const here before enum when this code is converted to js that would not be crazy 

enum SeatChoice {
    AISLE = "aisle",
    MIDDLE = "middle",
    WINDOW = "window",
    FOURTH = "fourth"
}

const hcSeat = SeatChoice.AISLE 

export {}

// iifi immediately invoked function 
