FROM node:17 as base

ENV WORKDIR=/app

WORKDIR $WORKDIR

COPY chart_app/package*.json ./

RUN npm install

FROM base

WORKDIR $WORKDIR

COPY chart_app/tsconfig*.json ./
COPY chart_app/vite.config.ts ./
COPY chart_app/env.d.ts ./
COPY chart_app/src ./src/
COPY chart_app/index.html ./

EXPOSE 3000

CMD ["npm", "run", "devd"]
