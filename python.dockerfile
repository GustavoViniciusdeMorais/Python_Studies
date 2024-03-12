FROM gustavovinicius/webserver:freenginx_python
WORKDIR /code
# RUN apk add --no-cache gcc musl-dev linux-headers
# RUN apk add tk
# # RUN pip install Django
# RUN apk add make automake gcc g++
# RUN pip install uvicorn[standard]
# RUN pip install "fastapi[all]"
EXPOSE 8000
ENTRYPOINT ["tail", "-f", "/dev/null"]