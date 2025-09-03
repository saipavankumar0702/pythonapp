from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
      <head>
        <title>Kubernetes Greeting</title>
        <style>
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f5f5f5;
          }
          h1 {
            color: #2d88ff;
            font-size: 2.5em;
            text-align: center;
          }
        </style>
      </head>
      <body>
        <h1>Sample python application!</h1>
      </body>
    </html>
    '''
