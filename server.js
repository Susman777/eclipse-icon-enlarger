var express = require('express');

var app = express();

app.use('/', function(req,res){
	res.send({
"user_1": {
		"name": "John",
		"checking": {
			"balance": "$37,043.31"
		}
	},


	"user_2": {
		"name": "Mary",
		"checking": {
			"balance": "$11,543.45"
		}
	},

	"user_3": {
		"name": "Susan",
		"checking": {
			"balance": "$72,436,851.84"
		}
	},

	"user_4": {
		"name": "Josh",
		"checking": {
			"balance": "$0.01"
		}
	},

	"user_5": {
		"name": "Michael",
		"checking": {
			"balance": "$80,432.45"
		}
	}
});
});

app.set( 'port', ( process.env.PORT || 5000 ));

// Start node server
app.listen( app.get( 'port' ), function() {
  console.log( 'Node server is running on port ' + app.get( 'port' ));
  });