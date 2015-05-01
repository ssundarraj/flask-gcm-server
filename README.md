# flask-gcm (under development)
A simple GCM message server in Flask.

Simple server that has an API to accept app IDs and store them, and a form that pushes notifications to all registered devices.

## Installation
``` python install.py```

To change any of the settings later, edit the `app/settings.py` file.

## Usage

### Run the server
``` ./manager.py ```

### API
To register a new device, the device should send a POST request to /addid with the parameter `reg_id` containing the GCM Registration ID. 
