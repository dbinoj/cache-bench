# cache-bench
Simple app to benchmark cache servers like ATS and Squid.

The app tries to download top alexa websites and their assets multiple times through a proxy and logs time taken.

## How To

- Install `python 2.7` and `pip` for your distribution
- Install virtual environment from pip: `pip install virtualenv`
- Run `source env/bin/activate` from project root
- Install requirements `pip install -r requirements.txt`
- Tweak options in bench.py if necessary
- Run `python bench.py`
- Enjoy. Logs for each website in logs/
