const express = require("express");
const dot = require("dot");
const path = require('path');
const sqlite3 = require('sqlite3'); // Corrected here
const bcrypt = require('bcrypt');
const session = require('express-session');
const crypto = require('crypto');
const app = express();
const db = new sqlite3.Database(':memory:');

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(session({
    secret: crypto.randomBytes(64).toString('hex'),
    resave: false,
    saveUninitialized: false,
}));

db.serialize(function() {
    db.run("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, user_regular TEXT)");
});

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.post('/register', async (req, res) => {
    let { username, password, user_regular } = req.body;
    let hashedPassword = await bcrypt.hash(password, 10);
    if (user_regular == '0' || user_regular==undefined){
      user_regular = '1'
    }
    db.run(`INSERT INTO users (username, password, user_regular) VALUES (?, ?, ?)`, [username, hashedPassword, user_regular], function(err) {
        if (err) {
            return res.status(500).send("Error registering user");
        }
        return res.status(200).send("User registered successfully");
    });
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    db.get(`SELECT * FROM users WHERE username = ?`, [username], async (err, row) => {
        if (err || !row || !await bcrypt.compare(password, row.password)) {
            return res.status(400).send("Invalid username or password");
        }
        req.session.userId = row.id;
        req.session.user_regular = row.user_regular;
        return res.status(200).send("Logged in successfully");
    });
});

app.get("/render", (req, res) => {
    let templateString = "";
    console.log(req.session.user_regular+"\n")
    console.log(parseInt(req.session.user_regular))
    if (!parseInt(req.session.user_regular) && req.session.user_regular !== undefined ) {
      templateString = req.query.template;
    }else {
      templateString = "Functionality not available for regular users!"
    }
    const template = dot.template(templateString);
    const output = template({});
    res.send(output);
});

app.listen(3000, () => {
    console.log("Server started on http://localhost:3000");
});