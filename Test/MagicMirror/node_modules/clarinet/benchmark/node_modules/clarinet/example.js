var clarinet = require("clarinet")

var parser = clarinet.parser();
parser.onvalue = function (v) {
  console.log("Value: " + v);
};
parser.onkey = function (key) {
  console.log("Key: " + key);
};
parser.onopenobject = function (key) {
  console.log("New Object, first key: " + key);
}
parser.oncloseobject = function () {
  console.log("Close Object");
}
parser.onopenarray = function () {
  console.log("New Array");
}
parser.onclosearray = function () {
  console.log("Close Array");
}
parser.onend = function () {
  console.log('End');
}

parser.write('{ "firstName": "John", "lastName" : "Smith", "age" : 25, "address" : { "streetAddress": "21 2nd Street", "city" : "New York", "state" : "NY", "postalCode" : "10021" }, "phoneNumber": [ { "type" : "home", "number": "212 555-1234" }, { "type" : "fax", "number": "646 555-4567" } ] }').close();
