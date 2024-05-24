import psutil

# Global variables
CRITICAL_RAM_THRESHOLD_PERCENT = 90
CRITICAL_DISK_THRESHOLD_PERCENT = 80
SEND_NOTIFICATION = True
DATA_TRACKING = False

class NotificationManager:

    def __init__(self):
        pass
            
    def __str__(self):
        return "A interface for managing notifications sent based on server metrics."
    
    def send_notification_email(self,total_disk, disk_usage, disk_usage_percent):
        subject = "Test Email"
        sender_email = ""
        recipient_email = ""
        plain_text = "This is a test email in plain text."
        html_content = "<html><body>\
                        <h1>DISK USAGE:</h1>\
                        <span>Total Disk: {0}</span>\
                        <span>Disk Used: {1}</span>\
                        <span>Disk Usage (percent): {2}%<span>\
                        </body></html>"
        
        # SMTP server configuration (example for Gmail)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        login = ""
        password = ""

        # Send the email
        self.send_email(subject, sender_email, recipient_email, plain_text, html_content, smtp_server, smtp_port, login, password)

    
    def send_email(self,subject, sender_email, recipient_email, plain_text, html_content, smtp_server, smtp_port, login, password):

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Create the email message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        # Attach both plain text and HTML versions of the message
        part1 = MIMEText(plain_text, 'plain')
        part2 = MIMEText(html_content, 'html')

        msg.attach(part1)
        msg.attach(part2)

        # Send the email
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Secure the connection
            server.login(login, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            print(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")

class DataTrackMonitor:

    def __init__(self):
        pass
    
    def __str__(self):
        return "A Interface to manage system data tracking"
    
    def send_data_to_api(self):
        pass




def get_system_usage():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=3)
    
    # Get RAM usage
    ram = psutil.virtual_memory()
    ram_total = ram.total / (1024 ** 3)  # Convert bytes to GB
    ram_used = ram.used / (1024 ** 3)    # Convert bytes to GB
    ram_percent = ram.percent
    
    # Get disk usage
    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024 ** 3)  # Convert bytes to GB
    disk_used = disk.used / (1024 ** 3)    # Convert bytes to GB
    disk_percent = disk.percent
    
    # Print system usage
    print(f"CPU Usage: {cpu_usage}%")
    print(f"RAM Total: {ram_total:.2f} GB")
    print(f"RAM Used: {ram_used:.2f} GB")
    print(f"RAM Usage: {ram_percent}%")
    print(f"Disk Total: {disk_total:.2f} GB")
    print(f"Disk Used: {disk_used:.2f} GB")
    print(f"Disk Usage: {disk_percent}%")

    return {'cpu_usage': cpu_usage, 'ram_total': ram_total, 'ram_used': ram_used, 'ram_percent': ram_percent, 'disk_total': disk_total, 'disk_used': disk_used, 'disk_percent': disk_percent}

if __name__ == "__main__":
    res = get_system_usage()

    if SEND_NOTIFICATION == True:
        NotificationManager().send_notification_email(res['disk_total'], res['disk_used'], res['disk_percent'])
    
    if DATA_TRACKING == True:
        pass
