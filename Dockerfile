FROM python:3.9
LABEL authors="fabiolana"

RUN pip install pandas

# ENTRYPOINT ["top", "-b"]