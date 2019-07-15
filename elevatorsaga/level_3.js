{
    init: function(elevators, floors) {
        var elevator = elevators[0];
        
        var requestedFloors = [];
        floors.forEach(function(floor) {
            floor.on("up_button_pressed down_button_pressed", function() {
                if(!requestedFloors.includes(floor)) {
                    requestedFloors.push(floor);
                }
            });
        });
        elevator.on("idle", function() {
            console.log("STATUS: idle");
            console.log("requestedFloors: " + [...requestedFloors].join(" "));
            if(requestedFloors.length > 0) {
                var nextRequestedFloor = requestedFloors.shift().floorNum();
                console.log("Going to requested floor: " + nextRequestedFloor);
                elevator.goToFloor(nextRequestedFloor);
            }
            var pressedFloors = elevator.getPressedFloors();
            pressedFloors.forEach(function(pressedFloor) {
                console.log("Going to pressed floor: " + pressedFloor);
                elevator.goToFloor(pressedFloor);
            })
            console.log("Processing destinationQueue: " + elevator.destinationQueue);
        });
    },
    update: function(dt, elevators, floors) {
    }
}
