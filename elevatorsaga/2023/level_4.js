// Needs work
{
    init: function(elevators, floors) {
        function getRandomNumber(max) {
            return Math.floor(Math.random() * max);
        }
        
        function getRandomElevator() {
            return elevators[getRandomNumber(elevators.length)];
        }
        
        for (let i = 0; i < elevators.length; i++) {
            let elevator = elevators[i];
            
            elevator.name = i;
            
            elevator.on("idle", () => {
                // go to all pressed floors
                if (elevator.getPressedFloors().length > 0) {
                    elevator.getPressedFloors().forEach((floor) => {
                        elevator.goToFloor(floor);
                    })
                }
            })
        }
        
        floors.forEach((floor) => {
            ["up_button_pressed", "down_button_pressed"].forEach((eventName) => {
                floor.on(eventName, () => {
                    // assign the floor to a random elevator
                    let elevator = getRandomElevator();
                    console.log(`assign elevator ${JSON.stringify(elevator)} to ${floor.floorNum()}`)
                    elevator.goToFloor(floor.floorNum());
                })
            })
        })
    },
    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}
