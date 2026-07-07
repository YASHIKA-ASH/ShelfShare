// =====================================
// ShelfShare Wishlist Module
// =====================================

checkLogin();

let wishlist = [];

// ----------------------------
// Load Wishlist
// ----------------------------

async function loadWishlist() {

    const userId = document
        .getElementById("wishlistUser")
        .value;

    if (!userId) {

        showToast(
            "Enter User ID",
            "error"
        );

        return;

    }

    try {

        showLoader();

        wishlist = await apiGet(

            `/wishlist/${userId}`

        );

        hideLoader();

        renderWishlist(wishlist);

    }

    catch (err) {

        hideLoader();

        showToast(

            err.message,

            "error"

        );

    }

}

// ----------------------------
// Render Wishlist
// ----------------------------

function renderWishlist(data) {

    const grid =
        document.getElementById("wishlistGrid");

    grid.innerHTML = "";

    if (!data || data.length === 0) {

        grid.innerHTML = `

        <div class="card">

        <h2>

        Wishlist Empty

        </h2>

        </div>

        `;

        return;

    }

    data.forEach(item => {

        grid.innerHTML += `

<div class="book-card">

<img src="${item.image_url || 'https://via.placeholder.com/250x300'}">

<div class="book-content">

<h3>

${item.title}

</h3>

<p>

<b>Author:</b>

${item.author}

</p>

<p>

<b>Subject:</b>

${item.subject}

</p>

<button

class="primary-btn"

onclick="borrowWishlist(${item.book_id})">

Borrow

</button>

<button

class="primary-btn"

style="margin-top:10px"

onclick="reserveWishlist(${item.book_id})">

Reserve

</button>

<button

class="primary-btn"

style="margin-top:10px;background:#ef4444"

onclick="removeWishlist(${item.id})">

Remove

</button>

</div>

</div>

`;

    });

}

// ----------------------------
// Borrow
// ----------------------------

async function borrowWishlist(bookId){

const userId=document
.getElementById("wishlistUser")
.value;

try{

await apiPost("/rentals/borrow",{

user_id:Number(userId),

book_id:Number(bookId),

issue_date:new Date()
.toISOString()
.split("T")[0],

due_date:new Date(
Date.now()+14*24*60*60*1000
).toISOString().split("T")[0]

});

showToast("Book Borrowed");

loadWishlist();

}

catch(err){

showToast(err.message,"error");

}

}

// ----------------------------
// Reserve
// ----------------------------

async function reserveWishlist(bookId){

const userId=document
.getElementById("wishlistUser")
.value;

try{

await apiPost("/reservations/",{

user_id:Number(userId),

book_id:Number(bookId)

});

showToast("Reservation Added");

}

catch(err){

showToast(err.message,"error");

}

}

// ----------------------------
// Remove
// ----------------------------

async function removeWishlist(id){

try{

await apiDelete(`/wishlist/${id}`);

showToast("Removed");

loadWishlist();

}

catch(err){

showToast(err.message,"error");

}

}

// ----------------------------
// Auto Load
// ----------------------------

window.onload=function(){

const user=localStorage.getItem("user_id");

if(user){

document.getElementById("wishlistUser").value=user;

loadWishlist();

}

}