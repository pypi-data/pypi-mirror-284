# Dash-Micro

This is a component to record audio from a device's built-in microphone within a Dash app

It wraps the Node.js package ```mic-recorder-to-mp3```.

By default, the component will render with only a "Record" and a "Stop"  button. As soon as something has been recorded, the user will also see a button to download the audio, as well as audio controls for playback (conditional rendering based on the presence or absence of an existing recording).

Because the component has built-in recording, stop, and audio controls, there are no required input properties except for the id. The relevant output prop if you want to use the resulting recording is ```fileUrl```, which is only possible to use if the file is POSTed back to the server (see note below).

## How to Use This

This component is in alpha, so feedback is much appreciated.

### Installation

```
pip install dash-micro
```

### How to use it in a Dash app:

```
import micro
from dash import Dash, callback, html, Input, Output, State

import flask
from flask import request
from pathlib import Path
import os
from werkzeug.datastructures import FileStorage


app = Dash(__name__)
server = app.server

app.suppress_callback_exceptions=True

# Define a route for POST requests to '/upload_audio' if you want to send the file somewhere for processing.
# Note that this is NOT REQUIRED if all you want to do is record and download the audio on a local client machine.
@server.route('/upload_audio', methods=['POST'])
def handle_upload():
    # print("file upload triggered!")
    if 'audioFile' not in request.files:
        return flask.jsonify({'error': 'No file part'}), 400
    
    file = request.files['audioFile']

    if file.filename == '':
        return flask.jsonify({'error': 'No selected file'}), 400
    if file:

        # Assume 'file' is your FileStorage object from the POST-ed file
        directory = '\\tmpfiles'
        os.listdir(directory)
        filename = file.filename
        file_path = os.path.join(directory, filename)

        # Check if the directory exists and create it if not
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Check if file exists and remove it to ensure overwrite -- app was originally not overwriting the existing file
        if os.path.exists(file_path):
            os.remove(file_path)

        file.save(file_path)
        # print("returning saved file_path")

        return flask.jsonify({'message': 'File uploaded successfully', "fileLoc": file_path}), 200


app.layout = html.Div([
    html.Div([
        micro.Micro(
            id='audioInput'
        ),
        html.Div(id='output'),
    ],
        style={"width": "20rem"}
    )
])


@callback(Output('output', 'children'), Input('audioInput', 'fileUrl'))
def display_output(value):

    if value is not None:

        # do something with the file here, e.g. send it to a transcription API

        return html.Div([
            html.P("You have saved the file at {}; use this fileUrl as the input to other functions.".format(value)),
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
```

### A couple of important things to know about this component: 

* If all you want to do is record audio in the browser and download the recordings, you can install and use this component without defining a method to post the audio to the server. As soon as you want to do additional file processing that requires you to send the audio somewhere (e.g. sending it to a STT engine via API), you must add a server route to POST the file to the server to your app (see example usage.py file).

* The built-in JS method ```navigator.getUserMedia``` requires a secure connection (https) to work. ```localhost``` is secure by default, so if you are using this component locally, there is no extra work required here. If you are hosting your app under a publicly accessible IP, then you will need to host it with a secure connection.

* This component works async – you press the start and stop buttons on it , and only after the stop is the full audio posted to the server so it can be further processed. It's explicitly not designed for real-time streaming audio, so it may not be suitable for something like a live conversational interface. 