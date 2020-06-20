# Zima 

### A Tornado Wrapper to Create REST API

1. pip install tornado
2. git clone https://github.com/reganto/zima.git 
3. cd zima
4. python app.py

**python app.py --help:**

```bash
usage: python app.py [options]

Zima is a wrapper around Tornado to create REST Api

optional arguments:
  -h, --help  show this help message and exit
  -p P        Run on the given port.(default is 8000)
  -m M        Run multiple instances of app.(default is 1)
  -l L        development,testing,production.(default is development)
  -t          Run unit tests.
  -v          Verbosity.
  -V          show program's version number and exit
    
```


### Example

```python
@route("/")
class HomeHandler(BaseHandler):
    def get(self):
        self.write({"status": "success"})
```


TODO:

- [x] Automatic nameing for routes (default route name is class lowercase name)
- [ ]  Integerate with SQLAlchemy
