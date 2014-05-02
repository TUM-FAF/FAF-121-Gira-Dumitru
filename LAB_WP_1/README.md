WINDOWS PROGRAMMING Laboratory Work #1
======================================

Window. Window handling. Basic window’s form elements
-----------------------------------------------------

<br>
##Completed Tasks
######Laboratory Work is done in Code::Blocks IDE

  - **Create a Windows application**

Open IDE, go to `File->New->Project->Win 32 GUI Project`. This is an example of the simplest Windows Application.

  - **Add 2 buttons to window: one with default styles, one with custom styles**

To create a button use `CreateWindowEx()` function with 2nd parameter `"BUTTON"`; this will make a default style button (ex: Submit, Clear).
For creating a custom style button, I've used `CreateFont()` function which let me define a new style, size, family for font. Then I've sent the font `buttonFont` to the object through `SendMessage()`. (ex: Red, Green, Blue).

  - **Add 2 text inputs to window: one with default styles, one with custom styles**

To create default text input I've used the `CreateWindowEx()` function as well, but now with `"EDIT"` as the 2nd parameter.
For a custom style, I've setted the text area to be Read-Only using `ES_READONLY` in the 4th parameter, created a new font with `CreateFont()` and sent it to the text area through `SendMessage` in the `WM_PAINT` message.

  - **Add 2 text elements to window: one with default styles, one with custom styles**

Text elements were created in `WM_PAINT` message with `DrawText()` function. To set another color for text, just use `SetTextColor()`

  - **Make elements to fit window on resize (1 pt)**

This is done by using in `WM_SIZE` message, the `MoveWindow()` function which has 2 important coordinates `LOWORD(lParam)` - stands for 'x' and `HIWORD(lParam)` - stands for 'y'. To limit min/max window size on resizing, use the `WM_GETMINMAXINFO` message and set `ptMinTrackSize/ptMaxTrackSize` parameters. 

  - **Make elements to interact or change other elements (0-2 pt)**
    - By clicking `Submit` button, the text from `textArea1` is sent to `textArea2`<br>
      The text from `textArea` is stored in `textStore` then is sent to `textArea` through `SendMessage(textArea2,      
      EM_REPLACESEL, 0, (LPARAM)textStore)`
