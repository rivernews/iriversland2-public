## Stage 1: Angular ##
##
##

FROM node:10-stretch-slim as ng_stage_image

ENV IMAGE_PROJECT_DIR /usr/src

# Copy project

WORKDIR ${IMAGE_PROJECT_DIR}

RUN mkdir -p ${IMAGE_PROJECT_DIR}/backend/frontend-bundle-dist && \
    mkdir -p ${IMAGE_PROJECT_DIR}/frontend

# Install dependencies
# for dev purpose, copy all including credentials
# for prod, you want to exclude credentials. Consider using a `.dockerignore` file. See https://stackoverflow.com/questions/43747776/copy-with-docker-but-with-exclusion
COPY frontend frontend

WORKDIR /usr/src/frontend

RUN npm i && npm rebuild node-sass

# only build dev; for production please add --prod
RUN $(npm bin)/ng build --prod






## Stage 2: Django ##
##
##

FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV IMAGE_PROJECT_DIR /usr/src

# Set work directory
# sets the working directory for docker commands e.g. RUN, CMD, ENTRYPOINT, COPY and ADD. 
# also WORKDIR will auto-create directory if not exist.
WORKDIR ${IMAGE_PROJECT_DIR}/backend

# Copy project
COPY backend .
COPY --from=ng_stage_image ${IMAGE_PROJECT_DIR}/backend/frontend-bundle-dist \
    ${IMAGE_PROJECT_DIR}/backend/frontend-bundle-dist

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && pip install -r requirements.txt

# vscode remote does not support EXPOSE, we use `appPort` in `.devcontainer.json` instead
# for production build, you might want to include EXPOSE
EXPOSE 8000

# Entry point script
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]
