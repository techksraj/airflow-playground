import json
import os
import shutil
import fileinput
TEMPLATE_FILE = 'include/templates/dynamic_dag_multifile_method.py'

for filename in os.listdir('include/data'):
    if filename.endswith('.json'):
        config = json.load(open(f"include/data/{filename}"))
        new_dagfile = f"dags/process_{config['dag_id']}.py"
        shutil.copyfile(TEMPLATE_FILE, new_dagfile)
        for line in fileinput.input(new_dagfile, inplace=True):
            line = line.replace('DAG_ID_HOLDER', config['dag_id'])
            line = line.replace('SCHEDULER_INTERVAL_HOLDER', config['schedule_interval'])
            line = line.replace('INPUT_HOLDER', config['input'])
            print(line, end='')