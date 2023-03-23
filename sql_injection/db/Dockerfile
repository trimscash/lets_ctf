FROM mysql:8

ENV MYSQL_ROOT_PASSWORD=root_pass
ENV MYSQL_DATABASE=ctfdb
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password_1111
ENV TZ=Asia/Tokyo

COPY my.cnf /etc/mysql/conf.d/my.cnf
COPY users.sql /docker-entrypoint-initdb.d/users.sql
COPY flag.sql /docker-entrypoint-initdb.d/flag.sql

EXPOSE 3306