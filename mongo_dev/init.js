client = new Mongo();
db = client.getDB('admin');
db.createUser(
  {
    user: "risk",
    pwd: "riskpassword",
    roles: [ { role: "root", db: "admin" }
            ]
  }
);

