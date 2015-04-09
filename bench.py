from joblib import Parallel, delayed
from subprocess import call
import multiprocessing, csv, os
from time import sleep
from datetime import datetime

SITES_CSV = "top-1m.csv" # Fields (w/o headers): serial no, url/hostname
REQUEST_COUNT = 1
LOG_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
WORK_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "work")
HOME_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Things which make my life easier
num_cores = multiprocessing.cpu_count() * 25
time_now = lambda: datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

# Create log, work dir
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)
if not os.path.exists(WORK_FOLDER):
    os.makedirs(WORK_FOLDER)

os.chdir(WORK_FOLDER)

r = csv.reader(open(os.path.join(HOME_FOLDER, SITES_CSV)))


# wget -p --no-cache -nd -nv --delete-after -e use_proxy=no -e http_proxy=172.16.0.2:8080 www.harvard.edu
# --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"

def processInput(site):
    print site
    for j in range(0, REQUEST_COUNT):
        call(
            [
                "time", 
                "wget", 
                "-p", 
                "--no-cache", 
                "-nd", 
                "-nv", 
                "--timeout=1", 
                "--tries=0", 
                "--span-hosts", 
                "-erobots=off", 
                "--delete-after", 
                "--user-agent=\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0\"",
                "-e use_proxy=yes", 
                "-e http_proxy=172.16.0.2:8080", 
                "--append-output=" + os.path.join(LOG_FOLDER, site),
                site
            ]
        )
    return True

results = Parallel(n_jobs=num_cores)(delayed(processInput)(row[1]) for row in r)

os.chdir(HOME_FOLDER)
print results
