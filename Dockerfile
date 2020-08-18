FROM python:3
ADD python_questions_and_answers.py

RUN pip install requests
RUN pip install io
RUN pip install json

CMD [ "python", "./python_questions_and_answers.py" ]
