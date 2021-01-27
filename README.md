# CODE-admission

Hello!
My name is Marzena and you are likely to be assessing my entry challenge for CODE.

Below listed are the components to my project:

#### WEBSITE
    Please take a look at the website I built. I used Wix, as this seemed like the most beginner-friendly interface. 

    The website can be seen published here: ENTER WEB ADDRESS FOR WIX.

#### DAG
    The second component to my work is a DAG - a process graph representing, at a high-level, the flow of data in my project. The DAG is also added to the website

#### COMPUTER VISION MODEL
    This component is the most challenging for me. I have worked with Kaggle and GitHub data to build a mockup, yes encountered several issues. I realised that this task was too ambitious for my skill level and had to abandon it dues to lack of time or necessary skill.
    I decided to keep this component as a placeholder and I hope to be lerning this during my first few semesters at CODE!

#### OPERATOR VERIFICATION WEBAPP MOCKUP
    One of the components has a human verification step, where a drope operator / manger / dispatcher spot-checks computer vision the model. This is a webapp mockup, built using Flask, and the purpose is to show that with a few clicks, the feedback loop can be returned to the model for prediction refinement.

    To run the Flask webapp, here are few requirements:
    - I am using Terminal in iOS, therefore my code is adapted to iOS
    - You must have Python and Flask installed: [Documentation here](https://flask.palletsprojects.com/en/1.1.x/installation/)
    - Clone my GitHub repo: (My GitHub page - top - Clone)
    - export FLASK_APP=flaskapp.py
    - export FLASK_DEBUG=1
    - flask.run
    Set the home directory to the [webapp] folder (cd webapp)
    ``` python flaskapp.py

    The terminal will return a http port, please paste in your web browser.
    To close the app port, Ctrl+C. To open the app, you will need to rerun the flaskapp.py command

    Your web should look like the following
    <img src="webapp_screenshot.png"
     alt="Webapp Should look Like This"
     style="float: left; margin-right: 10px;" />
