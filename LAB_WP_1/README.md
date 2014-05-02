WINDOWS PROGRAMMING Laboratory Work #1
======================================

Window. Window handling. Basic window’s form elements
-----------------------------------------------------

<br>
##Completed Taska
######Laboratory Work is done in Codeb::Blocks IDE

  - **Create a Windows application**

Open IDE, go to `File->New->Project->Win 32 GUI Project`. This is an example of the simplest Windows Application.

  - **Add 2 buttons to window: one with default styles, one with custom styles**

To create a button use `CreateWindowEx()` function with 2nd parameter `"BUTTON"`; this will make a default style button (ex: Submit, Clear).
For creating a custom style button, I've used `CreateFont()` function which let me define a new style, size, family for font. Then I've sent the font to the object through `SendMessage()`.

