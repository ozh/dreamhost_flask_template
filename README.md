# Flask template for Dreamhost


## How to:

* Install a recent Python3, see on [DH](https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3).
* Install a virtual env, see on [Brett's](https://www.brettsbeta.com/blog/2020/07/flask-on-dreamhost-shared-website-hosting/)
* Use the following app structure and this project's files :

```
<~/yourproject.com>
.
|-- __pycache__
|   |-- stuff will go here
|   `-- ...
|-- app
|   |-- __pycache__
|   |   |-- stuff will go here
|   |   `-- ...
|   |-- app.py
|   `-- config.py
|-- passenger_wsgi.py
|-- public
|   |-- favicon.gif
|   `-- favicon.ico
|-- tmp
|   `-- restart.txt
`-- venv
    |-- stuff will go here
    `-- ...
 ```
 
## Sources:
* https://www.brettsbeta.com/blog/2020/07/flask-on-dreamhost-shared-website-hosting/
* https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3
* https://github.com/jprusik/dreamhost-flask-project-template/

