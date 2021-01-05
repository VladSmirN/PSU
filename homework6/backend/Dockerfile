FROM python
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONPATH "${PYTHONPATH}:/var/lib/docker/containers/backend/predictor-service-template/predictor/"
WORKDIR  /var/lib/docker/containers/backend
RUN git clone https://github.com/mkls6/predictor-service-template.git
WORKDIR  /var/lib/docker/containers/backend/predictor-service-template/
RUN   pip install -r requirements.txt  
EXPOSE 5000
CMD ["flask", "run"]
