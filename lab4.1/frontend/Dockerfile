# Этап сборки
FROM node:18 AS build
WORKDIR /app

# Установка Angular CLI
RUN npm install -g @angular/cli@latest

# Копируем package.json и устанавливаем зависимости
COPY package*.json ./
RUN npm install

# Копируем остальные файлы
COPY . .

# Сборка проекта
RUN ng build --configuration production

# Проверяем существование собранных файлов
RUN ls -la /app/dist/*

# Этап запуска
FROM nginx:alpine

# Копируем собранные файлы (используем правильный путь из angular.json)
COPY --from=build /app/dist/frontend /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]