# CIS 211 Lab 4 starter
# Build a fictional campus club or service information page.
# Read CIS_211_Lab4_Guide.pdf before editing this file.
# This starter runs, but its TODO sections are not a completed submission.

import streamlit as st

# TODO 1: Replace these values with your own fictional club or service details.
# Keep at least three key-value pairs. You may add more.
club_info = {
    "name": "Student Wellness Club",
    "day": "Wednesday",
    "time": "2:00 PM",
}

# TODO 2: Replace these sample strings with at least three relevant activities.
# During the list change check, add one new item and keep it in the final app.
activities = [
    "Guided meditation and breathing exercises",
    "Vision board and goal-setting workshops",
    "Stress free games and movie night",
]

st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")

# Remove this starter message when your page is complete.
st.write("Starter page: complete the TODO sections using the Lab 4 guide.")

st.header("Purpose:Supporting student's overall well-being"
          "Focus:Stress management,self-care and positive connections.")
# TODO 3: Use st.markdown() to write your own two- or three-sentence introduction.
# Include both **bold** and *italic* text inside your Python string.
# The handout explains triple quotes if your Markdown spans several lines.

st.header("Activities or services")
for activity in activities:
# Your Streamlit display instruction goes here
    
# TODO 4: Write a for loop that displays every value from activities.
# Use Streamlit output inside the loop. Do not type each activity again.
st.header("Day:Wednesday"
          "Time:2:00 PM")
# TODO 5: Display at least two dictionary values by looking them up by key.
# Give the displayed values meaningful labels such as Day and Time.

st.header("Students can bring a notebook."
          "Comfortable clothing is welcome."
          "New members are welcomed.")

# TODO 6: Use st.markdown() to display a three-item Markdown list.
# Add one meaningful, working external Markdown link.
# https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health

# TODO 7: Add at least three comments explaining your OWN completed code.
 #This list stores the activites offered by the Student Wellness Club.
#This loop displays each sctivity from the list.
#This dictionary stroes imporatnat inforamtion about the club meetings.
# TODO 8: Perform both change checks and complete the private submission template.
# Upload your final source files, links, reflection, and app screenshots to Brightspace.
