StackerHomeLab
===
Abstract:xxx
## Papar Information
- Title:  `DashHomeLab With MFA`
- Authors:  `Rui Paiva`
- Preprint: [https://arxiv.org/abs/xx]()
- Full-preprint: [paper position]()
- Video: [video position]()

## Install & Dependence
- authelia
- nginx proxu manager
- other service

% gerar password para o authelia
https://bcrypt-generator.com/

![auth.domain.com](image.png)

![auth.domain.com SSL](image-1.png)

Na aba Advanced do auth.domain.com, colocar:
```
location / {
set $upstream_authelia http://authelia:9091;
proxy_pass $upstream_authelia;
client_body_buffer_size 128k;

#Timeout if the real server is dead
proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;

# Advanced Proxy Config
send_timeout 5m;
proxy_read_timeout 360;
proxy_send_timeout 360;
proxy_connect_timeout 360;

# Basic Proxy Config
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $http_host;
proxy_set_header X-Forwarded-Uri $request_uri;
proxy_set_header X-Forwarded-Ssl on;
proxy_redirect  http://  $scheme://;
proxy_http_version 1.1;
proxy_set_header Connection "";
proxy_cache_bypass $cookie_session;
proxy_no_cache $cookie_session;
proxy_buffers 64 256k;

}
````

No Advanced do serviço:
```
location /authelia {
    internal;
    set $upstream_authelia http://172.18.0.3:9091/api/verify; # IP e porta do Authelia
    proxy_pass_request_body off;
    proxy_pass $upstream_authelia;
    proxy_set_header Content-Length "";
    
    # Timeout se o servidor real estiver inativo
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;
    client_body_buffer_size 128k;
    proxy_set_header Host $host;
    proxy_set_header X-Original-URL $scheme://$http_host$request_uri;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header X-Forwarded-Uri $request_uri;
    proxy_set_header X-Forwarded-Ssl on;
    proxy_redirect http:// $scheme://;
    proxy_http_version 1.1;
    proxy_set_header Connection "";
    proxy_cache_bypass $cookie_session;
    proxy_no_cache $cookie_session;
    proxy_buffers 4 32k;

    send_timeout 5m;
    proxy_read_timeout 240;
    proxy_send_timeout 240;
    proxy_connect_timeout 240;
}

location / {
    set $upstream_portainer http://192.168.10.3:80;  # IP e porta do serviço
    proxy_pass $upstream_portainer;

    auth_request /authelia;
    auth_request_set $target_url $scheme://$http_host$request_uri;
    auth_request_set $user $upstream_http_remote_user;
    auth_request_set $groups $upstream_http_remote_groups;
    proxy_set_header Remote-User $user;
    proxy_set_header Remote-Groups $groups;

    # Redirecionar para a página de login do Authelia se a autenticação falhar
    error_page 401 =302 https://auth.domain.com/?rd=$target_url;

    client_body_buffer_size 128k;
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;
    send_timeout 5m;
    proxy_read_timeout 360;
    proxy_send_timeout 360;
    proxy_connect_timeout 360;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header X-Forwarded-Uri $request_uri;
    proxy_set_header X-Forwarded-Ssl on;
    proxy_redirect http:// $scheme://;
    proxy_http_version 1.1;
    proxy_set_header Connection "";
    proxy_cache_bypass $cookie_session;
    proxy_no_cache $cookie_session;
    proxy_buffers 64 256k;
}
```


## Use
- config/users_database.yml
  ```
  users:
  mail@mail.com:
    displayname: "Your Name"
    password: "$argon2id$v=19$m=65536,t=3,p=4$seu-hash-aqui"
    email: "mail@mail.com"
    groups:
      - admins

  ```
- for test
  ```
  python test.py
  ```
## Pretrained model
| Model | Download |
| ---     | ---   |
| Model-1 | [download]() |
| Model-2 | [download]() |
| Model-3 | [download]() |


## Directory Hierarchy
```
stackerHomeLab
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── homelab
│   ├── .env
│   ├── cards
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_card_delete_publicipcard.py
│   │   │   ├── 0003_publicipcard.py
│   │   │   ├── 0004_delete_publicipcard.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   ├── views.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── core
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── dashboard
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── cards.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_card.py
│   │   │   ├── 0003_card_open_in_new_tab.py
│   │   │   ├── 0004_remove_card_created_at_remove_card_image_and_more.py
│   │   │   ├── 0005_card_open_in_new_tab.py
│   │   │   ├── 0006_remove_card_active_remove_card_data_and_more.py
│   │   │   ├── 0007_delete_card_delete_service.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── db.sqlite3
│   ├── manage.py
│   ├── requirements.txt
│   ├── static
│   │   ├── assets
│   │   │   ├── demo
│   │   │   │   ├── chart-area-demo.js
│   │   │   │   ├── chart-bar-demo.js
│   │   │   │   ├── chart-pie-demo.js
│   │   │   │   └── datatables-demo.js
│   │   │   └── img
│   │   │       └── error-404-monochrome.svg
│   │   ├── css
│   │   │   ├── dark.css
│   │   │   └── styles.css
│   │   ├── images
│   │   │   ├── fundo.jpg
│   │   │   ├── fundo_.jpeg
│   │   │   └── fundo_2.jpg
│   │   └── js
│   │       ├── datatables-simple-demo.js
│   │       └── scripts.js
│   └── templates
│       ├── 401.html
│       ├── 404.html
│       ├── 500.html
│       ├── cards
│       │   └── card_template.html
│       ├── charts.html
│       ├── dashboard
│       │   └── tools_dashboard.html
│       ├── dashboard.html
│       ├── includes
│       │   ├── base.html
│       │   ├── head.html
│       │   ├── navigation.html
│       │   ├── scripts.html
│       │   └── sidebar.html
│       ├── index.html
│       ├── layout-sidenav-light.html
│       ├── layout-static.html
│       └── two_factor
│           └── _base.html
└── README.md
```

## Code Details
### Tested Platform
- software
  ```
  OS: Debian unstable (May 2021), Ubuntu LTS
  Python: 3.8.5 (anaconda)
  PyTorch: 1.7.1, 1.8.1
  ```
- hardware
  ```
  CPU: Intel Xeon 6226R
  GPU: Nvidia RTX3090 (24GB)
  ```
### Hyper parameters
```
```
## References
- [paper-1]()
- [paper-2]()
- [code-1](https://github.com)
- [code-2](https://github.com)
  
## License

## Citing
If you use xxx,please use the following BibTeX entry.
```
```
