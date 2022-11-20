

        let arrayProducto =[]
        let Total = 0
        function sumaProductos(Valoritem, Producto) {
            arrayProducto.push(Producto)
          Total = Total + Valoritem
          document.getElementById("elTotal").innerHTML = "TOTAL: " + "$" + Total; 
          console.log(arrayProducto);
          document.getElementById("valorProducto").value = Total
          document.getElementById("listaProductos").value=arrayProducto
          return Total}
    
        function Limpiar() {
          Total=0
          document.getElementById("elTotal").innerHTML = "TOTAL: " + "$" + 0; }