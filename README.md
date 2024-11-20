StackerHomeLab
===
Abstract:xxx
## Papar Information
- Title:  `paper name`
- Authors:  `A`,`B`,`C`
- Preprint: [https://arxiv.org/abs/xx]()
- Full-preprint: [paper position]()
- Video: [video position]()

## Install & Dependence
- python
- pytorch
- numpy

## Dataset Preparation
| Dataset | Download |
| ---     | ---   |
| dataset-A | [download]() |
| dataset-B | [download]() |
| dataset-C | [download]() |

## Use
- for train
  ```
  python train.py
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
