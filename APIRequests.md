# Requests for API:

| Function Name  | Description                | Params  | Return Values  | Complete? |
| -------------  | ---                        | ---     | ---            | ---       |
| .getXAngleRaw()    | Updates X&Y position and returns raw X Poteometer data  | None    |  angle:int raw poteometer data of the X servo.    |    ✔️    |
| .getYAngleRaw()    | Updates X&Y position and returns raw Y Poteometer data  | None    |  angle:int raw poteometer data of the Y servo.    |    ✔️    |
| .setXAngle()    | Pass 0-270 in, Sends CMD for motor to turn  | angle: int The angle to turn servo   |  check:boolean If angle > 270, T   |    ✔️    |
| .setYAngle()    | Pass 0-180 in, Sends CMD for motor to turn  | angle: int The angle to turn servo    |  check:boolean If angle > 180, T    |    ✔️    |
| .pauseMovement()    | Gets current X&Y Degree, and sends movement CMD for that Degree   | None    |  None    |    ✔️    |
| .idle()    | Incraments servo pos 1 deg every 25 MS, gives slow idle state  | stopCon:Event exits the method when .isSet()  |  None    |    ✔️    |
| .fire()    | Fires one Shot  | None    |  None    |    :x:    |
| .led_state()    | sets Led state  |  state:bool sets led   |  None    |    :x:    |
| .getXAngle()    | Wrapper: calls .getXAngleRaw(), converts to Degrees  | None    |  angle:float The angle the X servo is in.    |    ✔️    |
| .getYAngle()    | Wrapper: calls .getYAngleRaw(), converts to Degrees  | None    |  angle:float The angle the Y servo is in.    |    ✔️    |
| .setXMin()    | Wrapper: calls .setXAngle(), Send 0 Degrees  | None    |  None    |    ✔️    |
| .setYMin()    | Wrapper: calls .setXAngle(), Send 0 Degrees  | None    |  None    |    ✔️    |
| .setXMax()    | Wrapper: calls .setXAngle(), Send 270 Degrees  | None    |  None    |    ✔️    |
| .setYMax()    | Wrapper: calls .setXAngle(), Send 180 Degrees  | None    |  None    |    ✔️    |
| ._updatePosition()   | Way to get current angle.  | None    |  angle:float The angle the servo is in.    |    ✔️     |
