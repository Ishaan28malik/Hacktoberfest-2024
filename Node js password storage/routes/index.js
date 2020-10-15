var express = require('express');
var router = express.Router();
var bcrypt = require('bcryptjs');
var mysql = require('mysql');
var bcrypt = require('bcryptjs');

var connection = mysql.createConnection({
  host: 'localhost:8000',
  user: 'root',
  password: 'qwerty123',
  database: ''
});

/* GET home page. */
router.get('/', function (req, res) {
  res.render('index', { title: 'Express' });
});

router.post('app/user/auth', async (req, res) => {
  try {
    const { name, password } = req.body;
    const hash = await bcrypt.hash(password, 10);
    await connection('users').insert({ user_name: name, password: hash });
    res.send(200).json('account created');
  }
  catch (e) {
    console.log(e);
    res.status(500).send('Something is not working');
  }
});

router.post('/app/user/auth', async (req, res) => {
  try {
    const { name, hashp } = req.body;
    const user = await connection('users').first('*').where({ user_name: name });
    if (user) {
      const Pass = await bcrypt.compare(hashp, user.password);
      if (Pass) {
        res.status(200).json('Status' = 'Success', 'UserID' = user_id);
      } else {
        res.json('Wrong credentials');
      }


    }
  }
  catch (e) {
    res.status(500).send('Something is not working');
  }
});

router.post('app/user', function (req, res) {
  const user_name = req.params.username;
  const pass = req.params.password;

});

router.get('/app/sites/list/?user:UserID', function (req, res) {
  const id = req.params.UserID;

})

router.post('app/sites?user={userID}', function (req, res) {
  const website = req.params.website;
  const user = req.params.username;
  const pass = req.params.password;
})


module.exports = router;
