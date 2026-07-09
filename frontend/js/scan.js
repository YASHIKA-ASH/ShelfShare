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
    catch(error){

        hideLoader();

        console.error(error);

        showToast("Scanning failed","error");

    }

}

// --------------------------
// Fill Detected Details
// --------------------------

function fillDetails(data){

document.getElementById("title").value=data.title||"";
document.getElementById("author").value=data.authors||"";
document.getElementById("publisher").value=data.publisher||"";
document.getElementById("edition").value=data.edition||"";
document.getElementById("subject").value=data.subject||"";
document.getElementById("isbn").value=data.isbn||"";
document.getElementById("description").value=data.description||"";

}