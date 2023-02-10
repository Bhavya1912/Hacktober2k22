setInterval(() => {
    d = new Date();
    const htime = d.getHours();
    const mtime = d.getMinutes();
    const stime = d.getSeconds();

   let hrotation = 30 * htime + mtime / 2;
   let mrotation = 6 * mtime;
   let srotation = 6 * stime;

    hour.style.transform = `rotateZ(${hrotation}deg)`;
    min.style.transform = `rotateZ(${mrotation}deg)`;
    sec.style.transform = `rotateZ(${srotation}deg)`;
}, 10);

    function changeName(){

        if(document.getElementById("text").innerHTML== "Dark Theam")
        {
           console.log( document.getElementById("text").innerText= "Light Theam");
        }

        else{
            console.log(document.getElementById("text").innerText="Dark Theam");
        }

    }

    function change_color(){
        changeName();
        document.getElementById("Dark").classList.toggle("light") 
    }