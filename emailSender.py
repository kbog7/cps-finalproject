
import smtplib, ssl, sys

def send(inp):

    port = 465  # For SSL
    password = "#vuoffeah11"
    #print("the CLI is %s" %(sys.argv[1]))
    message = inp
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("tt1862477@gmail.com", password)
        # TODO: Send email here
        server.sendmail("tt1862477@gmail.com", "51dcole97@gmail.com", message)