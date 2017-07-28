# Ys - Youtube Streamer

![Youtube Stream](https://user-images.githubusercontent.com/4528223/28712810-bbb7928c-73b6-11e7-86e6-eff4d76b94d8.gif)

------------------------

## Features

- Playing youtube music in background on mobile (Android and iOS)
- Lightweight bandwidth (it loads audio stream only)
- Small Memory and CPU consuming (no playing whole video for just music)
- Simple UI/UX
- Easy to deploy (Python server and Nginx)

## Installation

### Docker way

```bash
$ docker-composer up -d
```

### Heroku

```bash
$ heroku login
$ heroku git:remote -a [your-app-id]
$ git push heroku master
$ heroku open
```

### Manually

**Run Python server**

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ gunicorn server:api
```

**Reverse proxy by NGINX**

```
server {
    listen 80;
    server_name ys.example.com;

    root /home/user/Ys;

    location / {
            proxy_redirect off;
            proxy_pass http://127.0.0.1:8000;
    }
}
```

## Contributors

- @khanhicetea

## License

This project is licensed under the MIT license.
