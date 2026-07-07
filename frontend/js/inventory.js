// ======================================
// ShelfShare Inventory Module
// ======================================

checkLogin();

let copies=[];

// ----------------------------
// Load Copies
// ----------------------------

async function loadCopies(){

const id=document
.getElementById("bookId")
.value;

if(!id){

showToast("Enter Book ID","error");

return;

}

try{

showLoader();

copies=await apiGet(

`/books/${id}/copies`

);

hideLoader();

renderCopies(copies);

}

catch(err){

hideLoader();

showToast(err.message,"error");

}

}

// ----------------------------
// Render Copies
// ----------------------------

function renderCopies(data){

const table=document
.getElementById("copyTable");

table.innerHTML="";

if(data.length===0){

table.innerHTML=`

<tr>

<td colspan="6">

No Copies Found

</td>

</tr>

`;

return;

}

data.forEach(copy=>{

table.innerHTML+=`

<tr>

<td>${copy.id}</td>

<td>${copy.barcode}</td>

<td>${copy.rack}</td>

<td>${copy.status}</td>

<td>${copy.condition}</td>

<td>

<button
class="primary-btn"
onclick="markLost(${copy.id})">

Lost

</button>

</td>

</tr>

`;

});

}
// ----------------------------
// Mark Copy Lost
// ----------------------------

async function markLost(copyId){

    if(!confirm("Mark this copy as Lost?")){

        return;

    }

    try{

        showLoader();

        await apiPut(

            `/copies/${copyId}`,

            {

                status:"Lost"

            }

        );

        hideLoader();

        showToast(

            "Copy Marked Lost"

        );

        loadCopies();

    }

    catch(err){

        hideLoader();

        showToast(

            err.message,

            "error"

        );

    }

}

// ----------------------------
// Mark Available
// ----------------------------

async function markAvailable(copyId){

    try{

        showLoader();

        await apiPut(

            `/copies/${copyId}`,

            {

                status:"Available"

            }

        );

        hideLoader();

        showToast(

            "Status Updated"

        );

        loadCopies();

    }

    catch(err){

        hideLoader();

        showToast(

            err.message,

            "error"

        );

    }

}

// ----------------------------
// Update Condition
// ----------------------------

async function updateCondition(copyId){

    const condition=prompt(

        "Condition (Good/Fair/Damaged)"

    );

    if(!condition){

        return;

    }

    try{

        await apiPut(

            `/copies/${copyId}`,

            {

                condition:condition

            }

        );

        showToast(

            "Condition Updated"

        );

        loadCopies();

    }

    catch(err){

        showToast(

            err.message,

            "error"

        );

    }

}

// ----------------------------
// Delete Copy
// ----------------------------

async function deleteCopy(copyId){

    if(!confirm(

        "Delete this copy?"

    )){

        return;

    }

    try{

        await apiDelete(

            `/copies/${copyId}`

        );

        showToast(

            "Copy Deleted"

        );

        loadCopies();

    }

    catch(err){

        showToast(

            err.message,

            "error"

        );

    }

}

// ----------------------------
// Auto Refresh
// ----------------------------

window.onload=function(){

    const id=localStorage.getItem("book_id");

    if(id){

        document
        .getElementById("bookId")
        .value=id;

        loadCopies();

    }

}