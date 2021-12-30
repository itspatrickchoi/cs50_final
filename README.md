# My CS50 Final Project: A Productivity Dashboard

## Introduction Video/Demo

- Link: https://youtu.be/wjDFsRIRGtI

## Code Structure

Since my project is done as a Flask web application, the main structure consists of the app.py with other python files and the template folder which includes HTML files and the static folder which includes images or similar files and also JavaScript files.

- app.py, helper.py

  - Backend, handling data/database, triggering actions, passing along information to the frontend, handling errors, signin, singup, user sessions etc

- templates/

  - layout.html - Base layout for all other HTML files, to keep code slim and partly "automated"
  - frontpage.html - First page people see when not signed in, tells visitors what the website is about
  - signin.html, signup.html - Pages where users can sign in when they already signed up once, otherwise they can still sign up

## Resources

### Tutorials

- How to use Postgres, Mail Dummies https://www.youtube.com/watch?v=w25ea_I89iM
- Curvaceous Design (Section Transitions, SVG Morph) https://www.youtube.com/watch?v=lPJVi797Uy0
- From Figma to Code https://www.youtube.com/watch?v=zFxG1sglWBI
- Neuromorphic analog clock https://www.youtube.com/watch?v=weZFfrjF-k4&t=100s
- Using APIs https://www.youtube.com/watch?v=tFVdxGgJPCo&t=0s
- General quick references when needed https://www.w3schools.com
- More on Flask Databases https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
- I used many various helpful sites upon searching for further help, all sites I used are referenced directly in the corresponding code

### Products/Frameworks/Libraries

- Flask-SQLAlchemy
- pgadmin4
- mailtrap.io
- haikei.app
- KUTE.js
- tailwind.css
- tailwind ui
- (bootstrap)
- Figma
- ...

## Fun Facts

### Lines of code? Probably 1000+

- 53+304+11+110+94+119+164+220+55+15+12+123+307=1587
- The signin/signup/success HTML files have used especially many more lines than technically needed because of formatting
- So deduct around 135 lines
- There are inevitably also some empty lines and several comments
- Approx. no. of lines: **1000+**
- (Edit: Oh, also quite a few lines from the svg files, so surely 1000+)

### How much time did I spend on this?

I have begun with CS50 already in 2020 I believe but I had a hiatus, and then I started again sometime in 2021. And based on a tracking app I used **since around August** (now it's end of December), I had then spent at least over **200 hours in the span of 3 months** programming.
Over **120 hours** of that was spent on the CS50 course. I learned new things outside the project too, after all. But remember **the 120 hours must be just a fraction** since it excludes 8 problem sets out of the 10 problem sets/projects, though granted the last 2-3 projects were the biggest. For the final project I spent around **53 hours**.

### What did I learn?

#### Patience

The CS50 course was a long and challenging journey which took me countless hours. But I persevered and continued. I doubt even half of the people who started the course actually finished it. In the end, it was a fruitful experience that let me learn a lot. So takeaway? Good things take time.

#### Growth Mindset

Closely linked to patience is the incredible progress you see throughout the journey and thus the improvement potential one can possess. It is honestly crazy for me to think I started with just building simple Super Mario staircase blocks in a certain constellation through algorithms, and progressed to building image filters from scratch over to playing detective investigating a crime with SQL over to building a full-stack web application letting people buy/sell virtual stocks with real-time prices. It just goes to show what one can achieve if one commits to improving. Growth mindset ftw!

#### Actual Programming/Coding Skills

Yes, I did actually learn a lot about programming, of course. Having actual challenges to face in forms of projects/problem sets really helped immensely. Even if the process is arduous, once you completed the project it feels so satisfying. And you feel great accomplishment and just look forward to the next challenge. Well, not surprisingly one will also feel overwhelmed or frustrated sometimes, and you question your life haha. But in the end, all the resources are available to you. Articles, videos and even forums aka StackOverflow or Discord where people can give you tips if you are really stuck. Sometimes even if you don't get a direct answer, you will later come up with one yourself.

Some of the hard skills I learned:

- Building a full-stack web application
- Usage of Flask framework together with Python, PostgreSQL as backend, and HTML, CSS and JavaScript as frontend
- How to use Visual Studio Code which was a lot tougher than I expected, I had used many other IDEs before like Eclipse, PyCharm, IntelliJ, R Studio, CS50 IDE,...But I had a lot of configuration issues with VSCode on my Windows (I actually basically took a break off CS50 and tried learning how to set up VSCode and then eded up doing The Odin Project for a while which also required me to learn how to operate a Virtual Machine (Linux Xubuntu) and the Terminal. Since with the VM I had a clean state I guess my VSCode was less messed up here.)
- How to deploy a project to Heroku (making it publicly available) (Haven't deployed this project yet, but I have learned how to do it before)
- How to use web design frameworks like Bootstrap and Tailwind
- How to make use of tools like haikei, KUTE.js to incorporate pattern designs and SVGs that can even be animated
- How to send emails automatically when conditions are met
- How to make use of design softwares like Figma and incorporate them into your code
- How to use database programs like pgadmin4
- How to create tables in databases for your project, how to link them properly to your website, so that with end user interaction, the database will update, insert, delete or send data (the hard part was finding out the specific syntax required for PostgreSQL with Flask)
- How to retrieve real-time information from APIs like those from a weather API provider
- Implementing instant-searchbars
- Various CSS tricks and knowledge one acquires throughout
- ...

Probably there are still things I forgot to mention. Fact is I learned quite some stuff.

### Future updates?

- Deploy on Heroku
- Theme design change
- Proper weather display
- Clock update to also display digital clock
- Have tags assignable to tasks items
- Filter view for tasks
- Display of stats such as streaks of succesfully completed foci
- Not just have streaks but have an entire point/score system, the better you do, the higher score you get
- Maybe have a global leaderboard
- Visualization of stats in e.g. graphs/curves etc
- Actual email notifications
- Add minigames like rock-paper-scissors, Tic-Tac-Toe etc
- ...

You have more ideas or feedback? Tell me!

Contact details on my website: itspatrickchoi.com
