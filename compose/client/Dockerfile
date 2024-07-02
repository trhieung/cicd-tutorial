FROM node:18

# Setting working directory. All the path will be relative to WORKDIR
WORKDIR /usr/src/app

# Copying package.json and package-lock.json
COPY services/client/package*.json ./

# Installing dependencies
RUN npm i

# Copying source files
COPY services/client/ .

# Installing pm2 globally
RUN npm install pm2 -g

# Command to start the development server
CMD ["npm", "run", "dev"]
