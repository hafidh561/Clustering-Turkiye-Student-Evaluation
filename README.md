# Clustering Turkiye Student Evaluation

Hello everyone, i make machine learning to clustering dataset turkiye and **my conclusion** is cluster this data becomes `Type of Student`. Iam use `Python` and some library to make this machine learning. You can try this model on this website [Turkiye Student Evaluation](https://hafidh561.github.io/Clustering-Turkiye-Student-Evaluation/). I deploy this model use `FLASK Restful-API` in `Heroku`.  
_Note: The response API took too long, be patient please_

---

## Tutorial Install Model

1. First you must have install `Python` and `Python Package Index` in your computer
2. After that, open directory [deploy_ml](./deploy_ml/) in your terminal
3. You can use virtual environments, if you want
4. Type in your terminal `pip install -r requirements.txt -y` and wait untill done
5. After that, type in your terminal `python app.py`

---

## Tutorial Use API

Connect in [Turkiye Student Evaluation Api](https://turkiye-student-evaluation-api.herokuapp.com/) and use `POST METHOD`

1. `q1` The semester course content, teaching method and evaluation system were provided at the start.
2. `q2` The course aims and objectives were clearly stated at the beginning of the period.
3. `q3` The course was worth the amount of credit assigned to it.
4. `q4` The course was taught according to the syllabus announced on the first day of class.
5. `q5` The class discussions, homework assignments, applications and studies were satisfactory.
6. `q6` The textbook and other courses resources were sufficient and up to date.
7. `q7` The course allowed field work, applications, laboratory, discussion and other studies.
8. `q8` The quizzes, assignments, projects and exams contributed to helping the learning.
9. `q9` I greatly enjoyed the class and was eager to actively participate during the lectures.
10. `q10` My initial expectations about the course were met at the end of the period or year.
11. `q11` The course was relevant and beneficial to my professional development.
12. `q12` The course helped me look at life and the world with a new perspective.
13. `q13` The Instructor's knowledge was relevant and up to date.
14. `q14` The Instructor came prepared for classes.
15. `q15` The Instructor taught in accordance with the announced lesson plan.
16. `q16` The Instructor was committed to the course and was understandable.
17. `q17` The Instructor arrived on time for classes.
18. `q18` The Instructor has a smooth and easy to follow delivery/speech.
19. `q19` The Instructor made effective use of class hours.
20. `q20` The Instructor explained the course and was eager to be helpful to students.
21. `q21` The Instructor demonstrated a positive approach to students.
22. `q22` The Instructor was open and respectful of the views of students about the course.
23. `q23` The Instructor encouraged participation in the course.
24. `q24` The Instructor gave relevant homework assignments/projects, and helped/guided students.
25. `q25` The Instructor responded to questions about the course inside and outside of the course.
26. `q26` The Instructor's evaluation system (midterm and final questions, projects, assignments, etc.) effectively measured the course objectives.
27. `q27` The Instructor provided solutions to exams and discussed them with students.
28. `q28` The Instructor treated all students in a right and objective manner.

_Note: q1-q28 the values must 1-5_

---

## Screenshots

- **Homepage**

![Index](./screenshots/screenshots_1.png 'Homepage')

- **Predict Appear**

![Predict](./screenshots/screenshots_2.png 'Predict Appear')

---

### License

[MIT](./LICENSE)

### Changelog

- **1.0 Clustering Turkiye Student Evaluation Release**

© Developed by [hafidh561](https://github.com/hafidh561).
