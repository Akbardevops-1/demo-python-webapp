FROM python

RUN pip install Flask jsonify

RUN git clone https://github.com

WORKDIR python-webapp

CMD ["python","./app.py"]
