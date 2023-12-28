# Flutter Notes 

## StatelessWidget & StatefulWidget
- A stateless widget never changes. Icon, IconButton, and Text are examples of stateless widgets. 
Stateless widgets subclass StatelessWidget.

- A stateful widget is dynamic: for example, it can change its appearance in response to events triggered by 
user interactions or when it receives data. Checkbox, Radio, Slider, InkWell, Form, and TextField are examples of 
stateful widgets. Stateful widgets subclass StatefulWidget.

## Gesture
For most common gestures, GestureDetector is used to detect tapping, dragging and long pressing.

InkWell is used for visual effects when the element is being tapped

GestureRecognizer is used to identify unique gesture and recognize simultaneous gestures multiple simultaneous gestures.

### GestureDetector
A non-visible widget to manage all gestures made within an application.

GestureDetector handles all the non-visible output, such as data.

### InkWell
A visible widget to visually displays the touch.

InkWell handles visible tapping effects.

### GestureRecognizer
GestureRecognizer goes beyond the Detector, it recognises simultaneous gestures or identify unique gesture.
For example: the RawGestureDetector widget detect multiple simultaneous gestures.

## Notes

To draw a line: [drawLine](https://api.flutter.dev/flutter/dart-ui/Canvas/drawLine.html).

Interactivity example: [Flutter Interactivity Example](https://docs.flutter.dev/ui/interactivity)

## Useful Examples
- getting start and end points of a line
[onPanStart/Update/End](https://blog.nonstopio.com/drag-and-drop-in-flutter-master-it-without-plugin-6957feef8d42)
