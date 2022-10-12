console.log("hola")
console.log(1+1)
let nombre = "Catalina"
let apellido = "Guerrieri"

let usuarioInstagram ={
    mail:"",
    telefono:"",
    usuario:"",
    contraseña:"",
    nombre:"",
    apellido:"",
    fechaDeNacimiento:"",
    cantDeFotos:"",
    usuariosQueSigue:"",
    usuariosSeguidores:"",

}
usuarioLinkedIn={
    id:"",
    nombre:"",
    aoellido:"",
    experienciaProfesional:"",
    formacionAcademica:"",

}


usuarios=[{
    "id": 1,
    "first_name": "Patrick",
    "last_name": "Doubleday",
    "email": "pdoubleday0@cafepress.com",
    "gender": "Male",
    "ip_address": "186.98.114.150"
  }, {
    "id": 2,
    "first_name": "Idalia",
    "last_name": "Godthaab",
    "email": "igodthaab1@1und1.de",
    "gender": "Female",
    "ip_address": "63.168.48.6"
  }, {
    "id": 3,
    "first_name": "Lucas",
    "last_name": "Tommasetti",
    "email": "ltommasetti2@sourceforge.net",
    "gender": "Male",
    "ip_address": "219.191.226.162"
  }, {
    "id": 4,
    "first_name": "Fey",
    "last_name": "Fletcher",
    "email": "ffletcher3@marriott.com",
    "gender": "Female",
    "ip_address": "159.156.190.221"
  }, {
    "id": 5,
    "first_name": "Franz",
    "last_name": "Kevane",
    "email": "fkevane4@shinystat.com",
    "gender": "Male",
    "ip_address": "142.216.93.149"
  }, {
    "id": 6,
    "first_name": "Jo",
    "last_name": "Voysey",
    "email": "jvoysey5@sciencedirect.com",
    "gender": "Genderfluid",
    "ip_address": "76.109.11.156"
  }, {
    "id": 7,
    "first_name": "Shaughn",
    "last_name": "Buxcey",
    "email": "sbuxcey6@paypal.com",
    "gender": "Male",
    "ip_address": "84.162.243.254"
  }, {
    "id": 8,
    "first_name": "Lotti",
    "last_name": "McKinie",
    "email": "lmckinie7@unc.edu",
    "gender": "Female",
    "ip_address": "207.159.78.63"
  }, {
    "id": 9,
    "first_name": "Steffen",
    "last_name": "Tresvina",
    "email": "stresvina8@altervista.org",
    "gender": "Male",
    "ip_address": "36.149.46.97"
  }, {
    "id": 10,
    "first_name": "Renault",
    "last_name": "Mumby",
    "email": "rmumby9@ustream.tv",
    "gender": "Male",
    "ip_address": "16.3.222.80"
  }]

console.table(usuarios)

const NOMBRES=['mari','valen','mateo']

console.log(NOMBRES)
console.log(NOMBRES[0]) //mari
const CARRITO=[]
console.log(CARRITO)
CARRITO.push("hola")
CARRITO.pop() //elimina el ultimo
CARRITO.unshift("Unshift")//agrega un elemneto al principio
