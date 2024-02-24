
# Project Title

This project creates a web application by using a Question Generation model in PyTorch.

## API Reference

#### Generate Question

```http
  POST /generate-question
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `context` | `string` | **Required**. Text for which you want to generate questions. |


```
curl -X POST -d "context=i live in paris" \
http://127.0.0.1:8000/generate-question
```

## Demo


[Link](https://drive.google.com/file/d/1FodjJiVC4Bkrkp-_hoM1KaRhZCtNCOIE/view?usp=sharing)

## Running locally

There are three methods for setting up the application locally and running, first is using the setup script, second manually and third using docker.

### Method-1: Use setup script

1. Go to root directory and give permission to script.sh to run.

```
chmod +x setup.sh
```

Run the script to install all dependencies.

```
./script.sh
```

2. Activate the virtual environment

```
source venv/bin/activate
```

3. Run your flask server

```
python app.py
```

Go to http://127.0.0.1:8000/ ! Your server is up.

### Method-2: Manual setup

1. It is recommended that you use virtual environment for running development server. If you don't want to use it, skip to step 4 directly.

```
python -m pip install --user virtualenv
```

2. If you're running the project for the first time, create a virtual environment.

```
virtualenv venv
```

3. Activate the virtual environment.

```
source venv/bin/activate
```

4. Install all the relevant depedencies by running this from the root directory of the project.
```bash
  pip install -r requirements.txt  
```

5. Run your flask server

```
python app.py
```

Go to http://127.0.0.1:8000/ ! Your server is up.

## Screenshots

![App Screenshot](https://i.imgur.com/hi98NmU.jpeg)


## Running Tests

To run tests, run the following command

```python
  python test_app.py
```


## Tech Stack

**Client:** HTML, CSS, Javascript

**Server:** Flask, Python

