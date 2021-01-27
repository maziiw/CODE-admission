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

The DAG is also added inserted in my Wix website.

### COMPUTER VISION MODEL MOCKUP
This component was the most challenging. I have worked with Kaggle and GitHub data and several tutorials to build a mockup, yet, I realised that my skill level does not match the required level. In the /modelling folder I added a README.md file listing out some of the challenges I encountered, and that list is significant. I decided to keep this component as a placeholder and I hope to be adding to it during my first few semesters at CODE!

### OPERATOR VERIFICATION WEBAPP MOCKUP
One of the components has a human verification step, where a drone operator / manager / dispatcher spot-checks predictions made by the model. The predicted value is the likelihood of rubbish pollution being present in the image captured. This is a webapp mockup, built using Python module - Flask, and the purpose is to show a quick idea of how I envisage this verification step.

To run the Flask webapp, here are few requirements:
    - I am using Terminal in iOS, therefore my code is adapted to iOS
    - You must have Python and Flask installed: [Flask documentation here](https://flask.palletsprojects.com/en/1.1.x/installation/)
    
    - Clone my GitHub repo: (My GitHub page - top - Clone, then follow up in terminal)
    - export FLASK_APP=flaskapp.py
    - export FLASK_DEBUG=1
    - flask.run
 Set the home directory to the [webapp] folder
    
    - cd webapp
    - python flaskapp.py
    - follow the port selected in terminal 

 The terminal will return a http port, please paste in your web browser.
    To close the app port, Ctrl+C. To open the app, you will need to rerun the python flaskapp.py command

 Your webapp should look like the following:
 
 <img src="webapp_screenshot.png" alt="Webapp Should look Like This" style="float: left; margin-right: 10px;" />
 
 
 ### Sources:
 Wix - create websites tutorials
 Corey Shafer - YouTube channel on building webapps
