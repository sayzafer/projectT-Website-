var cart = document.getElementById("carts");

function display_cart(cargo_cart){
    temp = "";

    for(var i = 0; i < type.length; i++){
        temp +=`
                <div class="row">
                    <div class="col-sm-4">
                      <center>
                        <img src="../static/img/cargo.png" width="80" height="60" alt="">

                      </center>
                    </div>

                    <div class="col-sm-1">
                      <center>
                        <img src="../static/img/type.png" id="tt" width="40" height="40" alt="">
                        <p style=" font-size: large;">${type[i]}</p>
                      </center>
                    </div>

                    <div class="col-sm-1">
                      <center>
                        <img src="../static/img/weightcrop.png" width="40" height="40" alt="">
                        <p style=" font-size: large;">${weight[i]}</p>
                      </center>
                    </div>

                    <div class="col-sm-1">
                      <center>
                        <img src="../static/img/volumecrop.png" width="40" height="40" alt="">
                        <p style=" font-size: large;">${volume[i]}</p>
                      </center>
                    </div>
                    
                    <div class="col-sm-1">
                      <center>
                        <img src="../static/img/value.png" width="40" height="40" alt="">
                        <p style=" font-size: large;">${value[i]}</p>
                      </center>
                    </div>

                    <div class="col-sm-1">
                      <center>
                        <img src="../static/img/boxcrop.png" width="40" height="40" alt="">
                        <p style=" font-size: large;">${nodeID[i]}</p>
                      </center>
                    </div>

                    <div class="col-sm-1">
                      <center>
                        <img src="../static/img/postakutusucrop.png" width="40" height="40" alt="">
                        <p style=" font-size: large;">${destNodeID[i]}</p>
                      </center>
                    </div>
                </div>  
              </div>
            </div>`
    }
    cart.innerHTML = temp;
}
display_cart(type)