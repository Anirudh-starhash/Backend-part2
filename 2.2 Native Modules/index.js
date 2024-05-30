const fs=require("fs")

// fs.writeFile("message.txt","Hello from node Js!",(err)=>{
//     if(err) throw err;
//     console.log("The file got saved!");
// });

fs.readFile("message.txt","utf-8",(err,data)=>{
    if(err) throw err
    console.log(data);
});