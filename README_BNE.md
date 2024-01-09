# Instalación API servidores BNE

### Requerimientos

1. git
2. sqlite3 >= 3.37
3. python3 >= 3.11
4. supervisord >= 4.2
5. nginx >= 1.14

### Instalación

1. Copiar repositorio en **/datos**

```
$ cd /datos
$ git clone https://github.com/vgenov-py/bne_api
```

2. Crear config.json

```
$ nano config.json
```

```json
{
	"SECRET_KEY": "Secreto más profundo",
	"DB_FILE": "instance/bne.db"
}
```

3. Crear base de datos de usuarios **users.db**

```
$ touch instance/users.db
```

4. Crear tabla **queries** en **users.db**

```
$ sqlite3 instance/users.db
```

```sqlite3
CREATE VIRTUAL TABLE queries USING FTS5 (id, query, length, date, dataset, time, is_from_web, error);
```

5. Crear entorno virtual python (**venv**)

* Verificar que el simbólico **python3** apunte a la versión correcta, **>= 3.11**, de no ser así, reemplazar python3 por python\<version\>

```
$ python3 venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

6. Verificar que la aplicación funcione

```
venv/bin/gunicorn main:app
```

7. Crear fichero de configuración **nginx**

```
$ nano /etc/nginx/conf.d/bne_api.conf
```

```nginx
server {
        listen 80;
        server_name <SERVER_NAME||IP_ADDRESS>;
        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
```

8. Crear fichero de configuración **supervisor**

```
$ touch /etc/supervisord.d/bne_api.ini
```

```supervisor
[program:bne_api]
directory=/datos/bne_api
command=/datos/bne_api/venv/bin/gunicorn --workers=6 main:app --timeout 120 --bind 127.0.0.1:8000
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/bne_api/bne_api.err.log
stdout_logfile=/var/log/bne_api/bne_api.out.log
```

* **--workers=6** debería ser el resultado de **CPU/s * 3**

9. Crear directorios y logs

```
$ mkdir /var/log/bne_api
$ touch /var/log/bne_api/bne_api.err.log
$ touch /var/log/bne_api/bne_api.out.log
```

10. Reiniciar nginx y supervisor 

```
$ nginx -t
$ nginx -s reload
$ systemctl restart supervisord.service
```

* La bandera/flag **-s** en el comando **nginx**, indicará si el fichero contiene algún error.


