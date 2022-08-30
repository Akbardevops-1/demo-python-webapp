FROM python
RUN pip install Flask jsonify
RUN git clone https://github.com/Akbardevops-1/demo-python-webapp.git
WORKDIR demo-python-webapp
CMD ["python","./app.py"]
