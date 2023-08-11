# Build stage
FROM node:14.17.6-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM python:3.8.12-slim-buster
WORKDIR /app
COPY --from=build /app/build /app/static
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev
COPY . .
CMD ["python", "app.py"]