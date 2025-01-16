# University_of_North_Texas_Attendance_11829107
Objective: Created a Python script for ease of taking attendance without pen and paper using face recognition
<br>
How it works<br>
1. setup the terminal in that file path and type python Attendance.py<br><br>
![first_setupattendance](https://github.com/user-attachments/assets/5823ff0d-53b0-47f7-84cb-34f18065e028)
<br>
2. Camera will be pop and it takes around 5-6 seconds<br><br>
![second_camerapopup](https://github.com/user-attachments/assets/abcc0bc2-e54e-4e2f-83bb-8778859facab)
<br>
3. If the image of the person is there in the database then it will match the face encodings and display the name of the person in front of the camera<br><br>
![third_recognizingandprintingthename](https://github.com/user-attachments/assets/4708b424-00c9-4fe9-8f4a-e97378a3c1d2)
<br>
4. This person is not there in the database and it shows unknown person<br><br>
![fourth_Unkownpersonshown](https://github.com/user-attachments/assets/3d5abaed-01e0-44d0-b204-26a58fa124b7)
<br>
5. Email has been sent successfully with the attachment and it will quit the program by using the q word on keyboard<br><br>
![fifth_emailsendsuccessfullyandquit](https://github.com/user-attachments/assets/f76f2986-678b-4645-a78f-db7ea361b318)
<br>
6. see the email which was shared<br><br>
![sixth_emailsentwithattachment](https://github.com/user-attachments/assets/0f3c18ed-258d-4fc5-ae45-a0204635410f)
<br><br>
#setup
<br><br>
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

