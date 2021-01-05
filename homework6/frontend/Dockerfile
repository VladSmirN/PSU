FROM python
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV PYTHONPATH "${PYTHONPATH}:/var/lib/docker/containers/frontend/web-page-template/src/"
WORKDIR  /var/lib/docker/containers/frontend
RUN git clone https://github.com/VladSmirN/web-page-template.git
WORKDIR  /var/lib/docker/containers/frontend/web-page-template/
RUN   pip install -r requirements.txt  
EXPOSE 5000
CMD ["flask", "run" ]


