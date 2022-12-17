## Demo exercise for a basic web server

### Getting started:

#### Install Python libraries:

```
pip3 install -r requirements.txt
```

Run the program:

```
uvicorn server:app
```

For VSCODE debugging:

```
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "server:app"
            ],
            "jinja": true,
            "justMyCode": true
        }
```
