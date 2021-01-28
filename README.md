# CODE-admission

Hello!
My name is Marzena and you are likely to be assessing my entry challenge for CODE.

Listed below are the components to my project:

### WEBSITE
Please start with taking a look at [my website](https://maziiw.wixsite.com/code-takeme). This page gives a good understanding of the idea behing the project. Please watch short videos on the Home page and the The Project page.

To build this page, I used Wix, as it seemed like the most beginner-friendly interface.

### DAG - Design Architechture Graph
The second component to my work is a DAG - a process graph representing, at a high-level, the flow of data in my project. 
The design can be accessed with [this link to Lucidchart](https://lucid.app/lucidchart/invitations/accept/5a5dd57a-ba2c-4b35-b729-de1df90ae760);
or, by following back to my website: [Design Architecture page](https://maziiw.wixsite.com/code-takeme/design-architecture)

#### COMPUTER VISION MODEL
This component is the most challenging for me. I have worked with Kaggle and GitHub data to build a mockup, yet encountered several issues (listed below). 

I realised that this task was too ambitious for my skill level and had to abandon it due to lack of time or necessary experience.

I decided to keep this component as a placeholder and I hope to be lerning this during my first few semesters at CODE!

Challenges I encountered:
   - working with virtual environments / or as the tutorial suggests - Anaconda venv
   - pros and cons of using Docker / Poetry
   - debugging
   - Visual Studio showing errors which Terminal solves
   - nvidia CUDA toolkit not supported for iOS


### OPERATOR VERIFICATION - WEBAPP MOCKUP
One of the components in my project has a human verification step, where a drone operator/dispatcher assesses predictions made the model. 

The predicted value is the likelihood of rubbish pollution being present in the image captured (but, as I mentioned in my video on 'What', it could also be identification of pest species). 

This webapp mockup was built using Python module Flask, and it represents a simple vision of this step.

To run the Flask webapp, here are few requirements:

I am using Terminal in iOS, therefore my code is adapted to iOS:

   - You must have Python and Flask installed: [Flask documentation here](https://flask.palletsprojects.com/en/1.1.x/installation/)
   - export FLASK_APP=flaskapp.py
   - export FLASK_DEBUG=1
   - flask.run

Clone my GitHub repo: (My GitHub page - top - Clone, then follow up in terminal)

Set the home directory to the webapp folder

    - cd webapp
    - python flaskapp.py
    - paste the port number displayed in terminal in web browser

 Your webapp should look like the following:
 
 <img src="webapp_screenshot.png" alt="Webapp Should look Like This" style="float: left; margin-right: 10px;" />
 
      My website should provide a screen recoding should you have issues running the app.

 ### What I Learned:
 I had so much fun with this assignement. Prior to starting I had some knowledge with Git, bash and Python environments.
 After the assignement, I also know how to:
 - build a website using Wix;
 - edit videos with iMovie;
 - overlay Star Wars Theme Song on top of my screen recodings! (I hope it was your favourite part too);
 - use Flask to build basic webapps;
 - use Visual Studio Code in a more proficient manner;
 - use basic OpenCV commands to read images;
 - set up a virtual environment (unfortunately this is where it stopped);
 - set up standardised form for Lucidchart flowcharts.

 ### Thank You!
Thank you for the time you spent looking through this assignement. I hope that you will find my work at a sufficient level to allow me to progress further. I am looking forward to be hearing from you!

 ### Literature and Tutorials Used:
- [Wix website making tutorials online](https://www.youtube.com/watch?v=7R3ZywgdCZI)
- [Corey Shafer YouTube channel on building webapps and other help](https://www.youtube.com/user/schafer5)
- [RealPython](https://realpython.com/python-virtual-environments-a-primer/)
- [Tensorflow tutorial by EdjeElectronics](https://github.com/tensorflow/models)
