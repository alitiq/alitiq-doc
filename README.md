# alitiq-doc
alitiq Documentation


## For testing the current content run: 

docker run --rm -it -p 8000:8000 -v $(pwd):/docs squidfunk/mkdocs-material

## Build static site

docker run --rm -v $(pwd):/docs squidfunk/mkdocs-material build