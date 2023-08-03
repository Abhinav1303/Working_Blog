from flask import Flask,render_template,request
import requests
import smtplib
blog_data=requests.get("https://api.npoint.io/3ce6d0075f0097d9370d")
blog_data_unpacked=blog_data.json()
app=Flask(__name__)


OWN_EMAIL = "cbabhinav@gmail.com"
OWN_PASSWORD = "abhinavbala02"

@app.route('/')
def runner():
    return render_template("seperated.html",blog_posts=blog_data_unpacked)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/<int:index>")
def for_post(index):

    for blog_post in blog_data_unpacked:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)




@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if(__name__=="__main__"):
    app.run(debug=True)