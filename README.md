## Poltician Tracker
#### Built using Django, JS (jQuery, Angular, maybe some d3), HTML and CSS

##### 3/17/2015:

This is a project I'm working on to compile and display information on US politicians.  The information will draw from a number of APIs including Sunlight Foundation and Open Secrets.  Who knows where this will go.  Right now I have the following done(ish):
- Backend model for politicians
- Database populated with info drawn from wikipedia using population scripts
- Profile view and an individual politician's profile view
- Bootswatch theme (Yeti) installed
- Live search function for politician names that uses an AJAX request to populate a list client side then a jQuery/KEYUP initiated regex filter
- Profile pages populate with information from github.com/unitedstates
- Info pulled in from OpenSecrets, cached and displayed using Angular
- basic log-in/change password/profile system made
- subscription functionality working

Short-term goals:
- Pull in more information from relevant APIs server side
- Have information put into individual profile template
- Create some sort of evaluation system of politicians (likes/dislikes/change over time period)
- Add in a facebook-style news feed of recent events or discussions about certain politicians
- Create a comment/like system for these news entries/dicussions

Long-term ideas:
- Add in a "rabbit hole" widget so users can track where they're clicking -- three dimensional so you can "go back" pages in rabbit hole and follow different route. Basically an advanced, visual "back" button.


##### Screenshot
![alt tag](https://raw.githubusercontent.com/pfarnach/politician-tracker/master/screenshot.png)

