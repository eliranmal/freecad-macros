<p align="right">
  <img src="https://img.shields.io/badge/tested%20on-my%20box%20alone-lightseagreen"
       alt="tested on: my box alone" />
  <img src="https://img.shields.io/badge/FreeCAD%20forums%20browsed-281,894-2057a9"
       alt="FreeCAD forums browsed: 281,894" />
  <img src="https://img.shields.io/badge/who's%20your%20uncle-bob-lightskyblue"
       alt="who's your uncle: bob" />
</p>

# FreeCAD macros &nbsp; <sub><sub><sup><sup>_some much needed macros for FreeCAD_</sup></sup></sub></sub>

💻 📐 🤖


## setup
                      
- download or clone this reopsitory, and keep it somewhere accessible on your drive
- run the [install][1] script. if you have a custom user macros directory, pass it as the first argument
- bob is you uncle


## macros

as a general note, macro options can be passed as json via the document comment input field. see each macro's description for supported options.             

### [CaptureSave][2]

captures images of various points of view, saves them to the project's `/export` directory, and then saves the project.  

#### options

##### `view` 
###### type: *String*<br/>default value: `"current"` 

selects the desired camera view to be captured.  
possible values: `"left"`, `"right"`, `"top"`, `"bottom"`, `"front"`, `"rear"`, `"iso"`, `"iso-flipped"`, `"iso-cw"`, `"iso-ccw"`, `"all"` (which includes all of the above), `"current"`.

##### `reset_visibility`
###### type: *Boolean*<br/>default value: `false`

forces visibility toggles on objects in the scene before the capture. 

### [FlipView][3]

flips the view front to back, while maintaining camera elevation, and focuses the view to fit.

### [RotateViewClockwise][4]

similar to FlipView, but rotates the view clockwise.

### [RotateViewCounterclockwise][5]

similar to FlipView, but rotates the view counterclockwise.





[1]: /bin/install.sh
[2]: /macros/CaptureSave.py
[3]: /macros/FlipView.py
[4]: /macros/RotateViewClockwise.py
[5]: /macros/RotateViewCounterclockwise.py
