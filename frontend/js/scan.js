// --------------------------
// Fill Detected Details
// --------------------------
let uploadedImage = null;

// --------------------------
// Scan Book
// --------------------------

async function scanBook() {

    const file = document.getElementById("bookImage").files[0];

    if (!file) {
        showToast("Please select an image", "error");
        return;
    }

    uploadedImage = file;

    // Preview Image
    document.getElementById("preview").innerHTML = `
        <img src="${URL.createObjectURL(file)}"
             style="width:250px;border-radius:15px;">
    `;

    const formData = new FormData();
    formData.append("file", file);

    try {

        showLoader();

        const response = await fetch(API_BASE + "/scan/", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        hideLoader();

        fillDetails(data);

        showToast("Book scanned successfully");

    }
    catch(err){

        hideLoader();

        showToast("Scanning failed","error");

        console.error(err);

    }

}
function fillDetails(data){

document.getElementById("title").value=
data.title||"";

document.getElementById("author").value=
data.author||"";

document.getElementById("publisher").value=
data.publisher||"";

document.getElementById("edition").value=
data.edition||"";

document.getElementById("subject").value=
data.subject||"";

document.getElementById("isbn").value=
data.isbn||"";

document.getElementById("description").value=
data.description||"";

}

// --------------------------
// Save Book
// --------------------------

async function saveBook(){

const book={

title:document.getElementById("title").value,

author:document.getElementById("author").value,

isbn:document.getElementById("isbn").value,

publisher:document.getElementById("publisher").value,

edition:document.getElementById("edition").value,

subject:document.getElementById("subject").value,

description:document.getElementById("description").value,

branch:"Computer Science",

semester:5,

image_url:"",

owner_id:1

};

try{

showLoader();

await apiPost(

"/books/",

book

);

hideLoader();

showToast(

"Book Added Successfully"

);

setTimeout(()=>{

window.location.href="books.html";

},1000);

}

catch(err){

hideLoader();

showToast(

err.message,

"error"

);

}

}

// --------------------------
// Clear Form
// --------------------------

function clearForm(){

document.getElementById("title").value="";

document.getElementById("author").value =
(data.authors || []).join(", ");

document.getElementById("publisher").value="";

document.getElementById("edition").value="";

document.getElementById("subject").value="";

document.getElementById("isbn").value="";

document.getElementById("description").value="";

document.getElementById("preview").innerHTML="";

document.getElementById("bookImage").value="";

uploadedImage=null;

}

// --------------------------
// Drag & Drop Support
// --------------------------

const upload=document.querySelector(".upload-box");

upload.addEventListener("dragover",e=>{

e.preventDefault();

upload.style.borderColor="#2563eb";

});

upload.addEventListener("dragleave",()=>{

upload.style.borderColor="#2563eb";

});

upload.addEventListener("drop",e=>{

e.preventDefault();

uploadedImage=e.dataTransfer.files[0];

document.getElementById("bookImage").files=e.dataTransfer.files;

document.getElementById("preview").innerHTML=`

<img
src="${URL.createObjectURL(uploadedImage)}"
style="width:250px;border-radius:15px;">

`;

});
window.scanBook = scanBook;
window.saveBook = saveBook;