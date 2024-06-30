https://www.mongodb.com/developer/languages/python/python-quickstart-crud/

Arch:
yay -S mongodb-bin
sudo systemctl status mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb  # start on boot

To create a MongoDB user account with administrator access [5]:
1. in /etc/mongodb.conf:
  #security:
  security:
    authorization: "disabled"

2. restart service:
  sudo systemctl restart mongodb

3. $ mongosh
  use admin
  admin> db.createUser( { user: 'admin', pwd: 'reddmon', roles: [{ role: 'root', db: 'admin' }] } );
  { ok: 1 }
  db.createUser(
    {
      user: "rich",
      pwd: "reddmon",
      roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
    }
  )

mongosh "mongodb://rich:reddmon@localhost:27017"

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

database user:
rich 9hzGTIA1HjKra6fG
rkba1 Hiu55xZe0buUedBd

# Install MongoDB Compass from AUR
yay -S mongodb-compass


Troubleshooting:
dotenv module not found - rerun poetry install
can't access Atlas -
db.createUser(
  {
    user: 'admin',
    pwd: 'reddmon',
    roles: [ { role: 'root', db: 'admin' } ]
  }
);

MongoDB Connection Error: SSL handshake failed:
add ip to atlas