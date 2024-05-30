import express from "express"
import { dirname } from "path"
import { fileURLToPath } from "url"
import bodyParser from "body-parser"

const app=express()
const port=3000
const _dirname=dirname(fileURLToPath(import.meta.url));

app.use(bodyParser.urlencoded({extended:true}));

app.use(express.static("public"));

app.get("/", (req,res)=>{
    res.render(_dirname+"/views/index.ejs");
});

app.get("/blog", (req,res)=>{
    res.render(_dirname+"/views/blog.ejs");
});

app.get("/about", (req,res)=>{
    res.render(_dirname+"/views/about.ejs");
});

app.get("/contact", (req,res)=>{
    res.render(_dirname+"/views/contact.ejs");
});

app.listen(port, ()=>{
    console.log(`The Server is listening on port ${port}`);

});

