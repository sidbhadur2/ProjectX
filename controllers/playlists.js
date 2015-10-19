var pg = require('pg');
var conString = process.env.DATABASE_URL || "postgres://aashna956:Charu@956@localhost:5432/projectx";
exports.createTable=function(req,res){
	var client = new pg.Client(conString);
	client.connect();
	var query = client.query("CREATE TABLE songs"+
									"("+
										"name character varying(50),"+
										"artist character varying(60)"+
									");");
	query.on("end", function(result){
		client.end();
		res.write('Table Schema Created');
		res.end();
	});
};
exports.addRecord=function(req, res){

        var client = new pg.Client(conString);

        client.connect();
        var query = client.query("insert into	songs (name, artist) "+ 
                               "values ('"+'random song'+"','"+ 'random artist'+"')");
    
        query.on("end", function (result) {          
            client.end(); 
            res.write('Success');
            res.end();  
        });

   };
exports.dropTable=function(req,res){
	var client = new pg.Client(conString);
	client.connect();
	var query = client.query("DROP TABLE songs");
	query.on("end", function (result) {
		client.end();
		res.write('Success');
		res.end();
        });
};