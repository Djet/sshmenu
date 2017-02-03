<!DOCTYPE html>
 <html>
   <head>
     <title>SSH Menu: Login</title>
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <!-- Bootstrap -->
      <link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
    </head>
    <body>
      <script src="http://code.jquery.com/jquery.js"></script>
      <script src="static/bootstrap/js/bootstrap.min.js"></script>
     <div class="row-fluid">
      <div class="span4 offset2">Enter</div>
     </div>
      <div class="container">
      <form class="form-horizontal" method="post" action="login">
        <div class="control-group">
          <label class="control-label" for="inputEmail">Email</label>
          <div class="controls">
            <input type="login" id="inputEmail" placeholder="Login">
          </div>
        </div>
        <div class="control-group">
          <label class="control-label" for="inputPassword">Password</label>
          <div class="controls">
            <input type="password" id="inputPassword" placeholder="Password">
          </div>
        </div>
        <div class="control-group">
          <div class="controls">
            <label class="checkbox">
              <input type="checkbox"> Remember me
            </label>
            <button type="submit" class="btn">Sign in</button>
          </div>
         </div>
       </form>
      </div>
    </form>
    </body>
 </html>

