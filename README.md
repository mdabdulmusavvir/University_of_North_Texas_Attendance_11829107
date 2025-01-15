# University_of_North_Texas_Attendance_11829107
Objective: Created a Python script for ease of taking attendance without pen and paper using face recognition
<br>
#setup
1. You need to have Python 3.13 version
2. Then check if you have pip by using the command pip --version
3. Download cmake by using the command python -m pip install cmake
4. then, cmake --version in command line
5. Copy the path of cmake which is shown in the above command result
6. then do window+s and environment varaibles and open it
7. under the user variable click on edit
8. go to the path and click new and paste the path which you have copied from the cmake path
9. then do all ok to commit the changes you made and restart the termial by closing it and opening it again
10. run this command python -m pip install opencv-python
11. then, python -m pip install face_recognition
12. now that every dependencies is installed.

You need to add the sender email and receiver email and sender email App password (https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237)
<br>
And also you need to do changes in the shared preferences.json file for the name and path of the image source, There is an example in shared prefernces.json file you can look into it, add the images of the people you want to do face recognition for attendance.

