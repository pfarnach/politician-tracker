## Poltician Tracker
#### Built using Django, JS (jQuery, Angular), HTML and CSS

##### 3/30/2015:

This is an app I'm working on as part of my final project at PDX Code Guild which will compile and display information on US politicians and will have room for user discussion.  The information will draw from a number of APIs including Sunlight Foundation and Open Secrets.  Who knows where this will go.  Right now I have the following done(ish):
- Backend model for politicians
- Database populated with info drawn from wikipedia using population scripts
- Profile view and an individual politician's profile view
- Bootswatch theme (Yeti) installed
- Live search function for politician names that uses an AJAX request to populate a list client side then a jQuery/KEYUP initiated regex filter
- Profile pages populate with information from github.com/unitedstates
- Info pulled in from OpenSecrets, cached and displayed using Angular
- Basic log-in/change password/profile system made
- Subscription functionality working
- Allow users to submit articles using Angular
- Allow users to upvote/downvote articles posted to politicians' pages

Short-term goals:
- Pull in more information from relevant APIs server side
- Have information put into individual profile template
- Create some sort of evaluation system of politicians (likes/dislikes/change over time period)
- Add in a facebook-style news feed of recent events or user-posted articles about politicians the user is subscribed to

Long-term ideas:
- Add in a "rabbit hole" widget so users can track where they're clicking -- basically, more interactive breadcrumbs so you can "go back" pages in rabbit hole and follow different route.


##### Screenshot
![alt tag](https://raw.githubusercontent.com/pfarnach/politician-tracker/master/screenshot.png)

