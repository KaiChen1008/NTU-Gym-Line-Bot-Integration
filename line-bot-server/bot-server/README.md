# ntu-gym-line-bot


## Installation

1. Prepare a https host
    - Apply a SSL certifates
    - Use ngrok (recommended)

2. Install libraries
```
pip install -r requirements.txt
```
	

## Usage

1. Launch ngrok

```
./ngrok http 8010
```

2. Launch django server

```
python manage.py runserver 8010
```
