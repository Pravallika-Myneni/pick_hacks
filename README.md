# Bear_Assays 
A tool to help you assays your mental and physical health and to understand the correlation

## Try Bear_Assays on your local system
- Clone our repository
- Download all the dependecies (streamlit, NLTK, text2Emotion, ...)
- To run streamlit app, use the follow command:
   ` streamlit run streamlit_app.py ` 

## 🧩 To use Viraam on your chrome browser
- Clone our repository only the folder of viraam
- Open [chrome://extensions/](chrome://extensions/) in your browser
- Toggle to switch to developer mode
- Click on "Load unpacked extension"
- Select the diretory of the cloned repo in your local system
- Tada🎉, now you can use Viraam on your system

## 💡Inspiration

At the end, every human of the day are left with themselves. its not about being alone but feeling lonely. 
we all would appreciate the help of a good listener. sometimes that is all we need. we can go to a therapist. Yes! we can. we can write it down in a dairy. yes we can but not all times we have time and facility for that.
Often we can see it for ourselves how the exercise we do and diet we take affects our mental health.
Bear_assays aids you  to analyze your mental and physical health. also to help you understand how inter-related they are and cheer you to take good care of them. 

##  👩🏻‍💻 What it Bear_assays?
- Asks the user to upload voice notes or write down what's running inside their head
- Interprets mood of the user
- Asks users to log the list of exercises and amount of sleep or their information from their fitness app(if any)
- Uses real world data collected from a smartwatch to help users understand the impact of physical health on mental health
- Calculates the number of calories burnt and displays a number of how much the workout contributed to their mood that day 
- Provides user with a Histogram of their sleep, mood, burnt calories
- A mini part of our project is a chrome extension called viraam which any user can download to take a healthy pause from your desk. Viraam makes you to step away from the computer and perform squats/stretching. Viraam helps you in making your workday routine more healthy.

##  🔨How we built
- we used Assembly AI API to convert audio to text 
- text2emotion python library to extract mood  from text
- seaborn and matplotlib to display heat-graph(shows relation between physical and mental activity)
- Streamlit to integrate everything and make the website

For Viraam
- We have implemented pose estimation provided by teachable machine 
- Developed chrome extension using HTML, CSS and Javascript (tensorflow.js)

## Challenges we ran into
- Brainstorming was a huge challenge
- Almost everything we implemented is new to both of us, so we had rough time learning and applying new libraries
- Emotion recognition is the hardest part

##🥇 Accomplishments that we're proud of
We are proud of the fact that we have built our first project together and the fact that we learned pretty much everything we implemented in past days only

## 📖What we learned
- Developing applications using steamlit
- Planning and Time management

## 🚀We will develop Bear_Assays further by:
-  Deploy the streamlit webapp so that everyone can access it
- Recommending songs after interpreting mood
- Including an option to log food intake
- To provide an option to interact with professional mental and physical health guiders 
- Create weekly and daily dash boards




