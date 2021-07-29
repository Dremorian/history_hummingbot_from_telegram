install

1. Go to directory for project 
cd var/www/history_hummingbot_from_telegram

2. Add virtual space at directory venv - $ python3.9 -m venv venv

3. activate venv by "source venv/bin/activate"
To Deactivate command "deactivate"
To full remove venv - "rm -r venv"

4. install packages from requirements.txt
pip install -r requirements.txt

Start

cd /var/www/history_hummingbot_from_telegram
source venv/bin/activate
python3 server.py
