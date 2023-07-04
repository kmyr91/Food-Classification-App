const express = require('express');
const multer  = require('multer');
const upload = multer({ dest: 'uploads/' });
const { exec } = require("child_process");
const path = require('path');  // <-- Add this line

const app = express();
const port = 3000;
const fs = require('fs');

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/index.html'));  // <-- Add this line
});

app.post('/predict', upload.single('image'), (req, res) => {
    exec(`python3 app.py ${req.file.path}`, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);  // <-- Add this line

        // Move the fs.readFile code inside the exec callback
        fs.readFile('prediction.txt', 'utf8' , (err, data) => {
            if (err) {
                console.error(err)
                return
            }
            res.send(`Prediction: ${data}`);
        });
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
