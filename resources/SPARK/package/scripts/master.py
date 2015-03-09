import sys
from resource_management import *
import subprocess

class Master(Script):
  def install(self, env):
    subprocess.call("/home/ubuntu/HDP-amazon-scripts/script/spark/spark_server.sh", shell=True)
  def stop(self, env):
    subprocess.call("/home/ubuntu/HDP-amazon-scripts/script/spark/spark_stop.sh", shell=True)
  def start(self, env):
    subprocess.call("/home/ubuntu/HDP-amazon-scripts/script/spark/spark_start.sh", shell=True)
     
  def status(self, env):
    print 'Status of the Sample Srv Master';
  def configure(self, env):
    print 'Configure the Sample Srv Master';
if __name__ == "__main__":
  Master().execute()
