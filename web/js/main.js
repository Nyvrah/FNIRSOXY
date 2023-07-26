var ambient = document.getElementById("deoxygenated");
var light1 = document.getElementById("oxygenated");
var table = document.getElementById("table");

document.getElementById("button").addEventListener("click", ()=>{eel.start()})

eel.expose(update_values)
function update_values(values, change){
  ambient.value = values[1]*1000;
  light1.value = values[0]*1000;
  new_row(values[0], values[1], change)
}

function new_row(a, b, change){
  var row = table.insertRow(1);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  cell1.innerHTML = a;
  cell2.innerHTML = b;
  cell2.style.backgroundColor = change[0]
  cell1.style.backgroundColor = change[1]
}