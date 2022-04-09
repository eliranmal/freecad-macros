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

<dl>
  <dt><a href="/macros/CaptureSave.py">CaptureSave</a></dt>
  <dd>
    captures multiple images of various points of view, saves them to the project's <code>/export</code> directory, and then saves the project.<br/>
    pass the desired view in the document comment (default is <code>current</code>). possible terms:<br/>
    <code>left</code>, <code>right</code>, <code>top</code>, <code>bottom</code>, <code>front</code>, <code>rear</code>, <code>iso</code>, <code>iso-flipped</code>, <code>iso-cw</code>, <code>iso-ccw</code>, <code>all</code>, <code>current</code>.    
  </dd>
  <dt><a href="/macros/FlipView.py">FlipView</a></dt>
  <dd>flips the view front to back, while maintaining camera elevation, and focuses the view to fit.</dd>
  <dt><a href="/macros/RotateViewClockwise.py">RotateViewClockwise</a></dt>
  <dd>similar to FlipView, but rotates the view clockwise.</dd>
  <dt><a href="/macros/RotateViewCounterclockwise.py">RotateViewCounterclockwise</a></dt>
  <dd>similar to FlipView, but rotates the view counterclockwise.</dd>
 </dl>



[1]: /bin/install.sh
