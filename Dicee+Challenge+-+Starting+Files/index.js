var randomnumber1=Math.floor(Math.random()*6)+1
var result1="./images/dice"+randomnumber1+".png"

var randomnumber2=Math.floor(Math.random()*6)+1
var result2="./images/dice"+randomnumber2+".png"

var x=document.querySelector(".img1").setAttribute("src",result1)
var y=document.querySelector(".img2").setAttribute("src",result2)

if(randomnumber2==randomnumber1){
    document.querySelector("h1").innerHTML="DRAW"
}
else if(randomnumber1>randomnumber2){
    document.querySelector("h1").innerHTML="Player1 Wins"
}
else{
    document.querySelector("h1").innerHTML="Player2 Wins"
}