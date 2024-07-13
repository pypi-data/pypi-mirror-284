import os
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def get_project_folder_name():
    project_folder_name = input("Enter the project folder name: ").strip()
    return project_folder_name

def zip_project_folder(folder_name):
    shutil.make_archive(folder_name, 'zip', folder_name)

def get_student_emails():
    student_emails = input("Enter student emails, comma separated: ").strip()
    emails = [email.strip() for email in student_emails.split(',')]
    return emails

def get_email_title():
    email_title = input("Enter the email title: ").strip()
    return email_title

def send_email_via_python(project_zip_path, recipient_emails, email_title):
    from_email = 'abhisheksharma.contact.me@gmail.com'
    password = 'tcxc jksa ajtd zrmc'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(recipient_emails)
    msg['Subject'] = email_title

    # Email body with HTML formatting
    body = f"""
    <html>
    <body>
        <h1 style="color: #4CAF50;">Online School of Programming</h1>
        <h2>Assignment Submission</h2>
        <p>Dear Student,</p>
        <p>We hope you are enjoying your learning journey with us. Please find attached your assignment project for review.</p>
        <h3>Assignment Details</h3>
        <ul>
            <li><strong>Project Folder:</strong> {os.path.basename(project_zip_path)}</li>
        </ul>
        <p>Make sure to go through the project and complete the required tasks. Don't just copy paste the project . Build your own one .If you have any questions, feel free to reach out to us.</p>
        <p>Best regards,</p>
        <p><strong>Online School of Programming Team</strong></p>
    </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))

    attachment = open(project_zip_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(project_zip_path)}')
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, recipient_emails, text)
    server.quit()

def delete_zip_file(zip_path):
    try:
        os.remove(zip_path)
        print("Successfully sent the attachment to students...")
    except Exception as e:
        print(f"An error occurred while deleting the zip file: {e}")

def main():
    while True:
        project_folder_name = get_project_folder_name()
        if os.path.isdir(project_folder_name):
            break
        else:
            print("Folder not found. Please enter a valid folder name.")
    
    zip_project_folder(project_folder_name)
    student_emails = get_student_emails()
    email_title = get_email_title()
    project_zip_path = f"{project_folder_name}.zip"
    
    send_email_via_python(project_zip_path, student_emails, email_title)
    delete_zip_file(project_zip_path)

if __name__ == "__main__":
    main()
