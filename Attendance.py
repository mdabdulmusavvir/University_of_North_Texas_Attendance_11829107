import cv2
import json
import numpy as np
import face_recognition
from datetime import datetime
from datetime import date
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    today = datetime.today()
    d1 = today.strftime("%m/%d/%Y")
    CurrentDay = date.today().strftime("%A")
    # Set up the email parameters
    sender_email = ".........@gmail.com"  # Replace with your email
    receiver_email = "......@my.unt.edu"  # Replace with professor's email
    if CurrentDay=="Thursday":
        subject = f"Attendance CSV File Data Analytics - {d1}"
        body = f"Dear Professor ,\n\nAttached is the attendance CSV file for the class Data Analytics 1 and date - {d1}.\n\nBest regards,\n\nYour Student\n Abdul Musavvir Mohammed\nreceiveremail@gmail.com\n11829107"
    elif CurrentDay=="Tuesday":
        subject = f"Attendance CSV File Large Data Visualization - {d1}"
        body = f"Dear Professor ,\n\nAttached is the attendance CSV file for the class Large Data Visualization and date - {d1}.\n\nBest regards,\n\nYour Student\n Abdul Musavvir Mohammed\nreceiveremail@gmail.com\n11829107"
    else:
        subject = f"Attendance CSV File - {d1}"
        body = f"Dear Professor,\n\nAttached is the attendance CSV file for the date - {d1}.\n\nBest regards,\n\nYour Student\n Abdul Musavvir Mohammed\nreceiveremail@gmail.com\n11829107"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the CSV file
    filename = "attendance.csv"  # The name of the file to send
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={filename}")
    
    msg.attach(part)

    # Send the email
    try:
        # Use Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, "Your App password/email passoword")  # Replace with your email password
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            message="Email sent successfully! bye"
            print("\n" + "*"*50)
            print(f"\033[1;34;40m{message}\033[0m")  # Green colored message
            print("*"*50)
            print("\n")

    except Exception as e:
        print(f"Failed to send email: {e}")


def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            today = datetime.today()
            d1 = today.strftime("%d/%m/%Y")
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString},{d1}')

def printBigMessage(message):
    # Print a big heading in the terminal
    print("\n" + "="*50)
    print(f"\033[1;32;40m{message}\033[0m")  # Green colored message
    print("="*50)

def takeAttendance():
    cam = cv2.VideoCapture(0)
    with open("sharedPreference.json", "r") as users_data_file:
        data = json.load(users_data_file)

    known_face_names = []
    known_face_encodings = []

    # Load user data and known faces
    for user in data["users"]:
        known_face_names.append(user["name"])
        try:
            image = face_recognition.load_image_file(user["img_path"])
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_face_encodings.append(encodings[0])
            else:
                print(f"Warning: No face found for {user['name']}")
        except Exception as e:
            print(f"Error loading image for {user['name']}: {e}")

    process_this_frame = True
    processed_names = set()  # Track names that have already been processed for attendance

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Resize frame to improve performance and convert to RGB
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  # Convert to RGB

        face_locations = []
        face_encodings = []
        face_names = []  # Ensure face_names is initialized here

        if process_this_frame:
            # Detect faces and get encodings
            face_locations = face_recognition.face_locations(rgb_small_frame)

            if face_locations:  # Only process if faces are detected
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    recognized_name = "Unknown"
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        recognized_name = known_face_names[best_match_index]

                    # Only process the face if it hasn't been processed yet
                    if recognized_name not in processed_names:
                        face_names.append(recognized_name)
                        markAttendance(recognized_name)
                        processed_names.add(recognized_name)
                        # Display "You're good!" in the terminal as a big message
                        printBigMessage(f"{recognized_name}, YOU'RE GOOD!")

        process_this_frame = not process_this_frame

        # Draw rectangles and labels around faces
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Show the frame continuously, no condition to stop showing
        cv2.imshow('Attendance Face Recognizer', frame)

        # Break loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            send_email()
            break

    cam.release()
    cv2.destroyAllWindows()

# Run the attendance function
if __name__ == "__main__":
    try:
        takeAttendance()
    except Exception as e:
        print(f"An error occurred: {e}")
