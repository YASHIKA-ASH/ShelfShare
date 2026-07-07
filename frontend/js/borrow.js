// =====================================
// ShelfShare Borrow Module
// =====================================

checkLogin();

let rentals = [];

// ---------------------------
// Load Borrowed Books
// ---------------------------

async function loadBorrowedBooks() {

    const userId = document
        .getElementById("userId")
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

        rentals = await apiGet(

            `/rentals/my-books/${userId}`

        );

        hideLoader();

        renderRentals(rentals);

    }

    catch (err) {

        hideLoader();

        showToast(
            err.message,
            "error"
        );

    }

}

// ---------------------------
// Render Rentals
// ---------------------------

function renderRentals(data) {

    const table =
        document.getElementById("borrowTable");

    table.innerHTML = "";

    if (!data || data.length === 0) {

        table.innerHTML =

        `<tr>

            <td colspan="7">

                No Borrowed Books

            </td>

        </tr>`;

        return;

    }

    data.forEach(rental => {

        table.innerHTML += `

<tr>

<td>${rental.id}</td>

<td>${rental.book_title || rental.book_id}</td>

<td>${rental.issue_date}</td>

<td>${rental.due_date}</td>

<td>${rental.status}</td>

<td>₹${rental.fine}</td>

<td>

<button

class="primary-btn"

onclick="returnBook(${rental.id})">

Return

</button>

</td>

</tr>

`;

    });

}
// ---------------------------
// Return Book
// ---------------------------

async function returnBook(rentalId) {

    if (!confirm("Return this book?")) {

        return;

    }

    try {

        showLoader();

        const response = await apiPost(

            `/rentals/return/${rentalId}`,

            {}

        );

        hideLoader();

        showToast("Book Returned Successfully");

        loadBorrowedBooks();

    }

    catch (err) {

        hideLoader();

        showToast(

            err.message,

            "error"

        );

    }

}

// ---------------------------
// Submit Rating
// ---------------------------

async function submitRating() {

    const rentalId = document
        .getElementById("ratingRentalId")
        .value;

    const rating = document
        .getElementById("rating")
        .value;

    if (!rentalId) {

        showToast(

            "Enter Rental ID",

            "error"

        );

        return;

    }

    try {

        showLoader();

        await apiPost(

            "/rentals/rate",

            {

                rental_id: Number(rentalId),

                rating: Number(rating)

            }

        );

        hideLoader();

        showToast(

            "Rating Submitted"

        );

    }

    catch (err) {

        hideLoader();

        showToast(

            err.message,

            "error"

        );

    }

}

// ---------------------------
// Refresh Table
// ---------------------------

function refreshBorrowedBooks() {

    loadBorrowedBooks();

}

// ---------------------------
// Auto Load
// ---------------------------

window.addEventListener(

    "load",

    () => {

        const userId = localStorage.getItem("user_id");

        if (userId) {

            document.getElementById("userId").value = userId;

            loadBorrowedBooks();

        }

    }

);