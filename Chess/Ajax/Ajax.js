console.log("this is my Rule")
let fetchbtn= document.getElementById('fetchbtn');
fetchbtn.addEventListener('click',buttonClickHandler)
function buttonClickHandler(){
    console.log('You have click the button');
    //instantiate an xhr object 
    const xhr =new XMLHttpRequest();
    // open the object
    xhr.open('Get','sagar.txt',true);
    xhr.onprogress=function(){
        console.log('On progress');

    }
    xhr.onload=function(){
        if(this.status +++ 200){
            console.log(this.responseText)

        }
        else{
            console.log("some Eroor Occred")
        }
        // console.log(this.responseText)
    }
    xhr.send();

}