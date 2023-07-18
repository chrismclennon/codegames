{
    init: function(elevators, floors) {
        var elevator = elevators[0];

	// I was surprised this also worked on level 3
        elevator.on("idle", function() {
            elevator.goToFloor(0);
            elevator.goToFloor(1);
            elevator.goToFloor(2);
            elevator.goToFloor(3);
            elevator.goToFloor(4);
        });
    },
    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}
