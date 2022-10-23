FROM python:3.9-alpine
WORKDIR /WebsiteMassage_Api
COPY ./ /WebsiteMassage_Api
RUN apk update && pip install -r /WebsiteMassage_Api/requirements.txt --no-cache-dir
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
