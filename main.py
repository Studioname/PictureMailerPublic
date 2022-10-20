import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# we iterate through a text file
# for each line in the file we:
# 1. trim whitespace
# 2. send it three pictures
# we do this in a try/catch block incase we encounter an invalid email address or sending error
# we only want to run the program once
# if the line is an empty string we skip over it
# we also create a text file which writes the index our loop has written up to
# that way in case of an error we can pick up from where we left off
# so we use the saved number as an iterator, we can create the text file ahead of time and set it to zero
# port 587

iterator_file = open("iterator.txt", "r")
iterator = int(iterator_file.readline().strip())
iterator_file.close()

# add non empty lines to a list of addresses
addresses_file = open("addresses.txt")
addresses = [address.strip() for address in addresses_file.readlines() if address.strip() != ""]
addresses_file.close()

email = "youremailaddress@here.com"
password = "youremailpassword"
smtp = "smtp-mail.youremailprovidersmtp.com"

#include the . at the start
image_type = ".jpg"


def add_image(msg, img_string, cid_ref):
    image_string = f"{img_string}{image_type}"
    image = open(image_string, 'rb')
    msgImage = MIMEImage(image.read())
    image.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', f'<{cid_ref}>')
    msg.attach(msgImage)
    return msg

# compose msg

msg = MIMEMultipart('related')

#email headers
msg['Subject'] = 'Subject here'
msg['From'] = email
msg['To'] = ""

# set the plain text body
html = """\
<html>
  <head></head>
    <body>
      <img src="cid:image1" alt="Brochure Page 1" style="width:75%;height:75%;"><br>
      <img src="cid:image2" alt="Brochure Page 2" style="width:75%;height:75%;"><br> 
      <img src="cid:image3" alt="Brochure Page 3" style="width:75%;height:75%;"><br>
    </body>
</html>
"""
# Record the MIME types of text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
msg.attach(part2)

# This example assumes the image is in the current directory
msg = add_image(msg, "picture0", "image1")
msg = add_image(msg, "picture1", "image2")
msg = add_image(msg, "picture2", "image3")

# iterate through addresses and send email
# if iterator == len(addresses):
#     iterator = 0

for address in addresses[iterator:]:

    msg['To'] = address
    # Send the message via local SMTP server.
    try:
        connection = smtplib.SMTP(smtp, port=587)
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email, address, msg.as_string())
        connection.quit()
    except smtplib.SMTPRecipientsRefused:
        print("Could not send mail to " + address + ".")

    #mark our position in the list
    iterator_file = open("iterator.txt", "w")
    file_body = str(iterator)
    iterator_file.write(file_body)
    iterator += 1
    iterator_file.close()