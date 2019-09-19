var counter = 1;
var limit = 5;
function addInput1(divName){
     if (counter == limit)  {
          alert("Maximum Limit of " + counter + " Products Reached !!");
     }
     else {
          var newdiv = document.createElement('div');
          newdiv.innerHTML =(counter + 1) + "<div class='form-group-inner'><div class='row'><div class='col-lg-4 col-md-4 col-sm-6 col-xs-6'>"+
          "<label class=''>Product ID</label><input type='text' class='form-control' />"+
          "</div><div class='col-lg-4 col-md-6 col-sm-6 col-xs-6'><label class=''>Product Name</label>"+
          "<select class='form-control'><option>{{ }}</option></select></div><div class='col-lg-4 col-md-4 col-sm-6 col-xs-6'>"+
          "<label class=''>Price Per 1kg/ltr</label><input type='text'  class='form-control' /></div></div></div>"+
          "<div class='form-group-inner'><div class='row'><div class='col-lg-4 col-md-4 col-sm-6 col-xs-6'><label class=''>Price Per 5kg/ltr</label>"+
          "<input type='text'  class='form-control' /></div><div class='col-lg-4 col-md-4 col-sm-6 col-xs-6'><label class=''>Price Per 25kg/ltr</label>"+
          "<input type='text'  class='form-control' /></div><div class='col-lg-4 col-md-4 col-sm-6 col-xs-6'><label class=''>Price Per 50kg/ltr</label>"+
          "<input type='text'  class='form-control' /></div></div></div>";
          document.getElementById(divName).appendChild(newdiv);
          counter++;
     }
}