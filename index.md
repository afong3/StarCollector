<!DOCTYPE html>
<html>

<body>
<head> 
<script src="jquery.js"></script> 
<script> 
$(function(){
$("#includedContent").load("b.html"); 
});
</script> 
</head> 
<h2>My First JavaScript</h2>

<button type="button"
onclick="document.getElementById('demo').innerHTML = Date()">
Click me to display Date and Time.</button>

   <h2>Stars Collected: 119 of 239</h2>
<html> 


  <body> 
     <div id="includedContent"></div>
  </body> 
</html>

<p id="demo"></p>

</body>
</html> 
