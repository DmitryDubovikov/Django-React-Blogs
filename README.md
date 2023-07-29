# Django-React-Blogs

Pre-commit:
```
pre-commit run --all-files
```

Run PostgreSQL DB in Docker:
```
docker run -d --name postgres_blogs_container -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -v postgres_blogs_data:/var/lib/postgresql/data postgres
```

Superuser:
```
Email: root@site.com
Username: root
Password: 1
```
