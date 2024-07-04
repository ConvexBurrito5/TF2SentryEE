# Requests for API:

DEFINE max_x_angle := 270
DEFINE max_y_angle := 180

| Function Name  | Description                | Params  | Return Values  | Complete? |
| -------------  | ---                        | ---     | ---            | ---       |
| ~~.getXAngleRaw()~~ helper method    | Updates X&Y position and returns raw X Poteometer data  | None    |  angle:int raw poteometer data of the X servo.    |    ✔️    |
| ~~.getYAngleRaw()~~ helper method    | Updates X&Y position and returns raw Y Poteometer data  | None    |  angle:int raw poteometer data of the Y servo.    |    ✔️    |
| .set_x_angle()    | Pass 0-max_x_angle in, Sends CMD for motor to turn  | angle: int The angle to turn servo   |  check:boolean If angle > max_x_angle, T   |    ✔️    |
| .set_y_angle()    | Pass 0-max_y_angle in, Sends CMD for motor to turn  | angle: int The angle to turn servo    |  check:boolean If angle > max_y_angle, T    |    ✔️    |
| .rotate_x_relative()    | increases the x servo angle by the specified amount ( can be negative) | angle: int The angle to turn x servo    |  returns True if 0<=new_angle<=max_x_angle else False   |    :x:    |
| .rotate_y_relative()    | increases the y servo angle by the specified amount ( can be negative)  | angle: int The angle to turn y servo    |  returns True if 0<=new_angle<=max_y_angle else False  |    :x:    |
| .pause_movement()    | Gets current X&Y Degree, and sends movement CMD for that Degree   | None    |  None    |    ✔️    |
| .idle()    | Increments servo pos 1 deg every 25 MS, gives slow idle state  | stopCon:Event exits the method when .isSet()  |  None    |    ✔️    |
| .fire()    | Fires one Shot  | None    |  None    |    :x:    |
| .led_state()    | sets Led state  |  state:bool sets led   |  None    |    :x:    |
| .get_x_angle()    | Wrapper: calls .getXAngleRaw(), converts to Degrees  | None    |  angle:float The angle the X servo is in.    |    ✔️    |
| .get_y_angle()    | Wrapper: calls .getYAngleRaw(), converts to Degrees  | None    |  angle:float The angle the Y servo is in.    |    ✔️    |
| .set_x_min()    | Wrapper: calls .setXAngle(), Send 0 Degrees  | None    |  None    |    ✔️    |
| .set_y_min()    | Wrapper: calls .setXAngle(), Send 0 Degrees  | None    |  None    |    ✔️    |
| .set_x_max()    | Wrapper: calls .setXAngle(), Send max_x_angle Degrees  | None    |  None    |    ✔️    |
| .set_y_max()    | Wrapper: calls .setXAngle(), Send max_y_angle Degrees  | None    |  None    |    ✔️    |
| ~~._update_position()~~ helper method   | Way to get current angle.  | None    |  angle:float The angle the servo is in.    |    ✔️     |
