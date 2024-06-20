https://www.mongodb.com/developer/languages/python/python-quickstart-crud/

Arch:
yay -S mongodb-bin
sudo systemctl status mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb  # start on boot
mongosh  $ mongo shell


To create a MongoDB user account with administrator access [5]:

$ mongosh

use admin
db.createUser(
  {
    user: "rich",
    pwd: "reddmon",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)

mongosh
Current Mongosh Log ID: 6671cf85da8f3b4261a26a12
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6
Using MongoDB:          7.0.11
Using Mongosh:          2.2.6
mongosh 2.2.9 is available for download: https://www.mongodb.com/try/download/shell

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

test>  db.getMongo()
mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6
test>

Atlas:
u: justin thyme
p: Q324@
e: rkba1
Cluster0
Your current IP address (172.59.8.51) has been added to enable local connectivity.
database user:
rkba1
Hiu55xZe0buUedBd

# Install MongoDB Compass from AUR
yay -S mongodb-compass


