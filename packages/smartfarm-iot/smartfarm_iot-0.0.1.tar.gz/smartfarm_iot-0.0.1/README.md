
<img src="./drag-logo.png" alt="LOGO" width="150" height="150" style="margin-bottom: -60px;">

[//]: # (![LOGO]&#40;./drag-logo.png&#41;)

# [Dr.AG Smart Farm IoT Project](http://www.doctor-ag.com/)

This project collects data from IoT devices in a smart farm using Modbus TCP protocol and publishes the data to an MQTT broker.

## Project Structure

- `config/`: Configuration files including farm information and device details.
- `src/`: Source code for reading Modbus data and publishing to MQTT.
- `logs/`: Directory for log files.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Setup

1. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Configure your MQTT broker and device information in the `config` directory.

3. Run the main program:
    ```bash
    python src/main.py
    ```

## Copyright

ⓒ 2024. NDS all rights reserved.

