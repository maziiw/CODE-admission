# CODE-admission

Hello!
My name is Marzena and you are likely to be assessing my entry challenge for CODE.

The project I chose has to do with the environmental impact of the rubbish pollution in the waterways. There are some businesses out there that already work on collecing rubbish from waterways, such as WasteShark, and I would like to add my ideas to their pile.

Below listed are the components to my project:

### WEBSITE
Please start with taking a look at [my website](https://maziiw.wixsite.com/code-takeme). This page gives a good understanding of the idea behing the project. 
I used Wix, as this seemed like the most beginner-friendly interface. Please watch the short videos and they should provide the necessary information regarding the project.

### DAG
The second component to my work is a DAG - a process graph representing, at a high-level, the flow of data and modelling in my project. 
[The design lives behind this link in Lucidchart](https://lucid.app/lucidchart/invitations/accept/5a5dd57a-ba2c-4b35-b729-de1df90ae760)

#### COMPUTER VISION MODEL
    This component is the most challenging for me. I have worked with Kaggle and GitHub data to build a mockup, yet encountered several issues (listed below). I realised that this task was too ambitious for my skill level and had to abandon it due to lack of time or necessary experience.
    I decided to keep this component as a placeholder and I hope to be lerning this during my first few semesters at CODE!

    Challenges I encountered:
      - working with virtual environments / or as the tutorial suggests - Anaconda venv
      - pros and cons of using Docker / Poetry
      - debugging
      - Visual Studio showing errors which Terminal solves
      - nvidia CUDA toolkit not supported for iOS

### OPERATOR VERIFICATION WEBAPP MOCKUP
One of the components has a human verification step, where a drone operator / manager / dispatcher spot-checks predictions made by the model. The predicted value is the likelihood of rubbish pollution being present in the image captured. This is a webapp mockup, built using Python module - Flask, and the purpose is to show a quick idea of how I envisage this verification step.

To run the Flask webapp, here are few requirements:
    - I am using Terminal in iOS, therefore my code is adapted to iOS
    - You must have Python and Flask installed: [Flask documentation here](https://flask.palletsprojects.com/en/1.1.x/installation/)
    - export FLASK_APP=flaskapp.py
    - export FLASK_DEBUG=1
    - flask.run

    - Clone my GitHub repo: (My GitHub page - top - Clone, then follow up in terminal)

 Set the home directory to the [webapp] folder
    - cd webapp
    - python flaskapp.py
    - paste the port number displayed in terminal in web browser

 Your webapp should look like the following:
 
 <img src="webapp_screenshot.png" alt="Webapp Should look Like This" style="float: left; margin-right: 10px;" />
 
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

 ### Literature Used:
[Wix website making tutorials online] (https://www.youtube.com/watch?v=7R3ZywgdCZI) 
[Corey Shafer YouTube channel on building webapps and other help](https://www.youtube.com/user/schafer5)
[RealPython](https://realpython.com/python-virtual-environments-a-primer/)
[Tensorflow tutorial by EdjeElectronics] (https://github.com/tensorflow/models)
