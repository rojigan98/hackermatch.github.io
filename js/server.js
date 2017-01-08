var tedious = require('tedious');
var Connection = tedious.Connection;  
var config = {  
    userName: 'hackmatch',  
    password: 'hackvalley123!',  
    server: 'hackmatch.database.windows.net',  
    options: {encrypt: true, database: 'AdventureWorks'}  
};  
var connection = new Connection(config);  
connection.on('connect', function(err) {  
    // If no error, then good to proceed.  
    console.log("Connected");  
});  

var Request = require('tedious').Request;  
var TYPES = require('tedious').TYPES;


function myFunction(){
	console.log("suh dude");
}