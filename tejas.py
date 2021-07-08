#!/usr/bin/python3

import cgi
from subprocess import getoutput
import subprocess

print("content-type:text/html")
print("Access-Control-Allow-Origin:*")
print("")

form = cgi.FieldStorage()

cmd = form.getvalue("command")
def kube(custom_cmd):
    print(getoutput(f"sudo kubectl {custom_cmd} --kubeconfig /root/admin.conf"))

if ("launch" in cmd or "run" in cmd or "create" in cmd or "make" in cmd)  and "pod" in cmd:
    if "name" in cmd  and "is" in cmd:
        cmd1 = cmd.split()
        #print(cmd1)
        cmd_index = cmd1.index("name")
        name = cmd1[cmd_index+2]
        #print(name)
        img_name = cmd1[cmd1.index("image")+1]
        kube(f"run {name} --image {img_name}")


    elif "name" in cmd:
        cmd1 = cmd.split()
        #print(cmd1)
        cmd_index = cmd1.index("name")
        name = cmd1[cmd_index+1]
        #print(name)
        kube(f"run {name} --image centos")
        img_name = cmd1[cmd1.index("image")+1]
        kube(f"run {name} --image {img_name}")



elif ("create" in cmd  or  "launch" in cmd or  "make" in cmd) and  "deployment" in cmd:
        if "name" in cmd  and "is" in cmd and "image" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+2]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")
        elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")

        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")


elif "expose" in cmd and  "deployment" in cmd:
        if "name" in cmd  and "is" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+2]
            port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")
        elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")
        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
            port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")

elif ("increase" in cmd or "scale" in cmd or  "replicate" in cmd ) or  "replica" in cmd or "decrease" in cmd:
        cmd1 = cmd.split()

        number = cmd1[cmd1.index("to")+1]
        if "name" in cmd  and "is" in cmd and "image" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+2]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"scale deployment {name} --replicas={number}")
            kube("get pods")
        elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            kube(f"scale deployment {name} --replicas={number}")
            kube("get pods")
        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
            kube(f"scale deployment {name} --replicas={number}")
            kube("get pods")
elif ("get" in cmd or "show" in cmd or "display" in cmd) and "pod" in cmd:
    kube("get pods")

elif ("get" in cmd or "show" in cmd or "display" in cmd) and "deployment" in cmd:
    kube("get deployments")

elif ("delete" in cmd or "destroy" in cmd)  and ("everything" in cmd or "entire" in cmd):
    kube("delete all --all")

elif "delete" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("delete")
            name = cmd1[cmd_index+2]
            name1 = cmd1[cmd_index+1]
            kube(f"delete {name1} {name}")
 25  help.html 
@@ -0,0 +1,25 @@
<ul>
	<li><b>For Launching The Pods:</b></li>
<ol>
<li>use keywords launch/create/make and pod/pods</li>
<li>give pod name after the keyword name/name is </li>
</ol>
<li><b>For Running Deployment:</b></li>
<ol>
<li>use keywords launch/create/make and deployment</li>
<li>give deployment image name after the keyword image/name is </li>
</ol>
<li><b>For Expose Services:</b></li>
<ol>
<li>use keywords expose and deployment</li>
<li>give the port no. after the keyword 'port' </li>
</ol>
<li><b>For Scaling Replica:</b></li>
<ol>
<li>use keywords increase/decrease/scale/replicate/replica</li>
<li>give the no. of replica after the keyword 'to' </li>
</ol>
<li><b>For deleting the services and environment:</b></li>
<ol>
<li>use keywords 'delete' </li>
</ol>	
 80  index.html 
@@ -0,0 +1,80 @@
<!DOCTYPE html>
<html>
    <head>
        <title>

        </title>
    </head>
    <link rel="stylesheet" href="./styles.css">
<body>
  <center>
    <!-- <header>
        <ul>
         <li><a class="links" href="#user"><button class="signbutton" type="button">Sign in</button></a></li>
           <li><a href="#grid"><img class="grid" src="https://cdn3.iconfinder.com/data/icons/navigation-and-settings/24/Material_icons-01-11-512.png" title="Google apps"></a></li>
          <li><a href="#images">Images</a></li>
          <li><a href="#gmail">Gmail</a></li>
          </ul>  
    </header> -->
    <div class="logo">
      <img alt="Google" src="k8s.png">
    </div>
    <div class="bar">
      <input class="searchbar" type="text" title="Search" id="docker_input" onkeypress="mySearch(event)"  name="command" />
      <a href="#"> <img class="voice" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Google_mic.svg/716px-Google_mic.svg.png" title="Search by Voice"></a>

    </div>
    <div class="bar1" id = "display">
    <b>
    <pre>
waiting for yout request ...
    </pre>
    </b>
    </div>
    </div>
    <div class="buttons">
      <button class="button" type="button" onclick="mySearch()">Click to Run</button>
      <button class="button" type="button" onclick="myHelp()">Help</button>
     </div>
  </center>

  <script>
      function mySearch(e){
	      if (e.keyCode==13){

            docker_inp = document.getElementById("docker_input")
            docker_inp.value
            console.log(docker_inp.value)
            var xhr = new XMLHttpRequest();
            xhr.open("GET",'http://192.168.99.111/cgi-bin/gagan.py?command='+docker_inp.value,true);
            xhr.send();

            xhr.onload = function(){
                var output = xhr.responseText;
                document.getElementsByTagName("pre")[0].innerHTML=output;
                document.getElementsByClassName('bar')[0].style = "border-bottom-left-radius: 0px; border-bottom-right-radius: 0;border-bottom: 3px;"
            //    document.getElementsByClassName('bar')[0].style = "border-bottom-right-radius: 0;"
            //     document.getElementsByClassName('bar')[0].style = "border-bottom: 3px;"
            }
	      }
	      else{
		      document.getElementsByTagName("pre")[0].innerHTML="";
	      }

      }


function myHelp(){
            var xhr = new XMLHttpRequest();
            xhr.open("GET",'http://192.168.99.111/help.html',true);
            xhr.send();
	xhr.onload = function(){
                var myoutput = xhr.responseText;
		const parser = new DOMParser();
		const newoutput = parser.parseFromString(myoutput, "text/html");
		console.log(newoutput)
		alert(newoutput.documentElement.textContent);

}}
  </script>
  </body>
 BIN +5.53 KB k8s.png 
Binary file not shown.
 100  styles.css 
@@ -0,0 +1,100 @@
ul {
    list-style-type: none;
    overflow: hidden;
  }

  li {
    float: right;
  }

  li a {
    color: #000;
    display: block;
    text-align: center;
    padding: 10px 10px;
    text-decoration: none;
    font-size:14px;
  }
  li a:hover {
    text-decoration: underline;
  }
  .grid{
    height:23px;
    position:relative;
    bottom:4px;
  }

  .logo{
    margin-top:200px;
    margin-bottom:20px;
  }
  .bar{
    margin:0 auto;
    width:600px;
    border-radius:30px;
    border:1px solid #dcdcdc;
    z-index: 200;
  }
  .bar:hover{
    box-shadow: 1px 1px 8px 1px #dcdcdc;
  }
  .bar1:hover{
    box-shadow: 0px 8px 8px 1px #dcdcdc;
  }
  .bar:focus-within{
    box-shadow: 1px 1px 8px 1px #dcdcdc;
    outline:none;
  }
  .bar1:focus-within{
    box-shadow: 0px 1px 8px 1px #dcdcdc;
    outline:none;
  }
  .searchbar{
    height:45px;
    border:none;
    width:500px;
    font-size:16px;
    outline: none;

  }
  .bar1 {
    width: 600px;
    position: relative;
    border-radius: 0px;
    height: max-content;
    padding-top: 50px;
    border-bottom-left-radius: 30px;
    border-bottom-right-radius: 30px;
    top: -38px;
    border-top: none;
    z-index: 100;
    word-wrap: break-word;
  }
  .voice{
    height:20px;
    position:relative;
    top:5px;
    left:10px;
  }
  .buttons{
    margin-top:30px;
  }
  .button{
    background-color: #f5f5f5;
    border:none;
    color:#707070;
    font-size:15px;
    padding: 10px 20px;
    margin:5px;
    border-radius:4px;
    outline:none;
  }
  .button:hover{
    border: 1px solid #c8c8c8;
    padding: 9px 19px;
    color:#808080;
  }
  .button:focus{
    border:1px solid #4885ed;
    padding: 9px 19px;
  }
0 comments on commit 1e43da0
@jhatejasvi
 
 
