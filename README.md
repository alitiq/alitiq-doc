# alitiq-doc
alitiq Documentation


## For testing the current content run: 

docker run --rm -it -p 8000:8000 -v $(pwd):/docs squidfunk/mkdocs-material

## Build static site

docker run --rm -v $(pwd):/docs squidfunk/mkdocs-material build


## Run server with FastAPI

Build image: 

docker build -t "doc_image" .

docker run -d --name 'alitiq_doc' --rm -v /etc/letsencrypt/:/app/letsencrypt -v $(pwd):/app -p 443:443 doc_image:latest hypercorn app.server:app --bind 0.0.0.0:443 --workers 2 --keyfile /app/letsencrypt/live/docs.alitiq.com/privkey.pem  --certfile /app/letsencrypt/live/docs.alitiq.com/fullchain.pem
