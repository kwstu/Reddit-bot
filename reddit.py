import praw
import config
import time



def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "first app")
    print("Logged in!")
    return r

r = bot_login()

# Pictures
picture_subreddit = r.subreddit('RoastMe')
picture_submissions = picture_subreddit.top(limit = 30)


imglinks = []
commentbody = []
mods = picture_subreddit.moderator()

print("Collecting submissions...")
for picture_submission in picture_submissions:
    # if link contains JPG
    if "jpg" in picture_submission.url:
        imglinks.append(picture_submission.url)
        if picture_submission.num_comments > 1:
            if not picture_submission.comments[0].author in mods:
                commentbody.append(picture_submission.comments[0].body)
            elif not picture_submission.comments[1].author in mods:
                commentbody.append(picture_submission.comments[1].body)
            

print("Done collecting submissions")

while True:
  for i in range(0, len(imglinks)):
      print(imglinks[i])
      # CSS file
      html_file = open('style.css', 'w')
      html_file.write("body {  margin:0px; padding: 0px;width:100%;  height:100%;  background:url(\'" + imglinks[i] + "\') center center no-repeat;  background-size:contain;  overflow:hidden;  background-color:#121211;  position:relative;  font-family: tahoma; } #title {  position:absolute;  width:100%;  min-height:60px; text-align:center; color:#FFF;   bottom:5; line-height:60px; align:middle; font-weight: bold; font-size: 360%; }")
      html_file.close()

      # html file
      html_file = open("roasts.html", "w")
      html_file.write("<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" /><meta http-equiv=\"refresh\" content=\"10\"/></head>""<body><div id=\"title\">"+commentbody[i]+"</div></body></html>")
      html_file.close()

      time.sleep(10)

  break

