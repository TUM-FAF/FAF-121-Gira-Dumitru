IDE LABORATORY WORK #3
======================

Mobile Applications Development
-------------------------------

<br>
##Completed Tasks
######Laboratory work is done in Android Studio IDE

   - **Study design guidlines for any mobile OS**

I've got familiar with basic knowledges about design of Android application.

   - **Create a mobile app and launch it on emulator/simulator. Your app should have at least 3 element and one action **

I've used the built-in Android Studio emulator. <br>
My application contains elements of this kind `Spinner`, `TextView`, `EditText` and `Button`. <br>
The action is described by a popup which appears, when `Submit` button is clicked. `Toast.makeText(getApplicationContext(), "Configuration saved", Toast.LENGTH_LONG).show();`

   - **Install your application on a mobile phone. It should have somewhere your full name(2pt)**

In my project properties, I've set the `Minimum Required SDK - Android 2.2 (Froyo)` and `Target SDK - Android 4.4.2 (Kit Kat)` , so I was able to emulate the application on Android 2.3 version. <br>
My full name is shown in the 3rd tab of TabHost.

   - **Create 3 different views(2pt)**

In order to have 3 different views, I've created a TabHost which in the .xml looks like:
```<Tabhost>
     <LinearLayout>
       <TabWidget></TabWidget>
       <FrameLayout> 
         <LinearLayout> HERE is FIRST TAB </LinearLayout>
         <LinearLayout> HERE is SECOND TAB </LinearLayout>
         <LinearLayout> HERE is THIRD TAB </LinearLayout>
       </FrameLayout>
     </LinearWidget>
   </Tabhost>```

First view is page where user chooses an option using spinners, gives a name to configuration, and submits it.<br>
Second view is page where last configuration is shown. <br>
Third view is an about page.

   - **Create a responsive layout (1pt)**
Responsive layout was created by specifying custom values to `layout-width` in percentages.


###Program Overview
![overview](https://raw.githubusercontent.com/TUM-FAF/FAF-121-Gira-Dumitru/master/IDE/IDE_LAB_3/work.gif)




     
