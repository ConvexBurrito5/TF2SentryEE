# Requests for API:

| Function Name  | Description                | Params  | Return Values  | Complete? |
| -------------  | ---                        | ---     | ---            | ---       |
| servo.angle    | Way to get current angle.  | None    |  angle:float The angle the servo is in.    |    :x:    |
| servo.max      | Spin to max angle          | None    |  None          |    :x:    |
| servo.min      | Spin to min angle          | None    |  None          |    :x:    |
| servo.set_angle      | Spin to specified angle, abstract version of max and min.        | Angle:float    |  None          |    :x:    |
| servo.step_min | Way to step to min and have a way to terminate midway if an event (Python Event class) is set.         | event:Event the event to check for   |  None  |    :x:    |
| servo.step_max | Way to step to max and have a way to terminate midway if an event(Python Event class) is set.         | event:Event the event to check for    |  None   |    :x:    |
| shoot_one_shot    | Fire a single bullet.          | None    |  None          |    :x:    |
| Spray full auto | Shoot until event is set to false. | event: Event the event to check for | None | :x: |
| led.state | Update the LED STATE | led state | None | :x: |
