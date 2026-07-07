// ===============================
// ShelfShare Books Module
// ===============================

checkLogin();

let books = [];

let selectedBook = null;

// ===============================
// Load Books
// ===============================

window.onload = function () {

    loadBooks();

};

async function loadBooks() {

    try {

        showLoader();

        books = await apiGet("/books/available");

        hideLoader();

        renderBooks(books);

    }

    catch (err) {

        hideLoader();

        console.error(err);

        showToast(err.message, "error");

    }

}

// ===============================
// Render Books
// ===============================

function renderBooks(bookList) {

    const grid = document.getElementById("bookGrid");

    grid.innerHTML = "";

    if (!bookList || bookList.length === 0) {

        grid.innerHTML = `

        <div class="card">

            <h2>No Books Found</h2>

        </div>

        `;

        return;

    }

    bookList.forEach(book => {

        grid.innerHTML += `

        <div class="book-card">

            <img src="${book.image_url || 'https://via.placeholder.com/250x300'}">

            <div class="book-content">

                <h3>${book.title}</h3>

                <p><b>Author:</b> ${book.author}</p>

                <p><b>Subject:</b> ${book.subject}</p>

                <p><b>Status:</b> ${book.availability}</p>

                <button
                class="primary-btn"
                onclick="borrowBook(${book.id})">

                Borrow

                </button>

                <button
                class="primary-btn"
                style="margin-top:10px"
                onclick="wishlist(${book.id})">

                Wishlist

                </button>

                <button
                class="primary-btn"
                style="margin-top:10px"
                onclick="openModal(${book.id})">

                Add Copies

                </button>

            </div>

        </div>

        `;

    });

}
// ===============================
// Search Books
// ===============================

function searchBooks() {

    const keyword = document
        .getElementById("searchBox")
        .value
        .toLowerCase();

    if (keyword === "") {

        renderBooks(books);

        return;

    }

    const filtered = books.filter(book =>

        book.title.toLowerCase().includes(keyword) ||

        book.author.toLowerCase().includes(keyword) ||

        (book.subject || "")
            .toLowerCase()
            .includes(keyword)

    );

    renderBooks(filtered);

}

// ===============================
// Borrow Book
// ===============================

async function borrowBook(bookId) {

    const userId = prompt("Enter User ID");

    if (!userId) return;

    try {

        showLoader();

        await apiPost("/rentals/borrow", {

            user_id: Number(userId),

            book_id: Number(bookId),

            issue_date: new Date()
                .toISOString()
                .split("T")[0],

            due_date: new Date(
                Date.now() + 14 * 24 * 60 * 60 * 1000
            )
                .toISOString()
                .split("T")[0]

        });

        hideLoader();

        showToast("Book Borrowed Successfully");

        loadBooks();

    }

    catch (err) {

        hideLoader();

        showToast(err.message, "error");

    }

}

// ===============================
// Wishlist
// ===============================

async function wishlist(bookId) {

    const userId = prompt("Enter User ID");

    if (!userId) return;

    try {

        await apiPost("/wishlist/", {

            user_id: Number(userId),

            book_id: Number(bookId)

        });

        showToast("Added to Wishlist");

    }

    catch (err) {

        showToast(err.message, "error");

    }

}

// ===============================
// Add Copies Modal
// ===============================

function openModal(bookId) {

    selectedBook = bookId;

    document
        .getElementById("copyModal")
        .classList
        .remove("hidden");

}

function closeModal() {

    document
        .getElementById("copyModal")
        .classList
        .add("hidden");

}
// ===============================
// Submit Book Copies
// ===============================

async function submitCopies() {

    const count = parseInt(
        document.getElementById("copyCount").value
    );

    const rack = document
        .getElementById("rack")
        .value;

    if (!count || count <= 0) {

        showToast(
            "Enter valid number of copies",
            "error"
        );

        return;

    }

    try {

        showLoader();

        await apiPost(

            `/books/${selectedBook}/copies`,

            {

                count: count,

                rack: rack

            }

        );

        hideLoader();

        closeModal();

        showToast(
            "Copies Added Successfully"
        );

        loadBooks();

    }

    catch (err) {

        hideLoader();

        showToast(
            err.message,
            "error"
        );

    }

}

// ===============================
// Reserve Book
// ===============================

async function reserveBook(bookId) {

    const userId = prompt("Enter User ID");

    if (!userId) return;

    try {

        await apiPost(

            "/reservations/",

            {

                user_id: Number(userId),

                book_id: Number(bookId)

            }

        );

        showToast(
            "Reservation Successful"
        );

    }

    catch (err) {

        showToast(
            err.message,
            "error"
        );

    }

}

// ===============================
// Book Details
// ===============================

function viewBook(book) {

    alert(

`Title : ${book.title}

Author : ${book.author}

Subject : ${book.subject}

Publisher : ${book.publisher}

Edition : ${book.edition}

ISBN : ${book.isbn}

Availability : ${book.availability}`

    );

}

// ===============================
// Refresh Books
// ===============================

function refreshBooks(){

    document
        .getElementById("searchBox")
        .value="";

    loadBooks();

}

// ===============================
// Enter Key Search
// ===============================

document.addEventListener(

"DOMContentLoaded",

()=>{

const box=document.getElementById("searchBox");

if(box){

box.addEventListener(

"keyup",

function(e){

if(e.key==="Enter"){

searchBooks();

}

}

);

}

}

);