// ===============================
// ShelfShare Dashboard
// ===============================

checkLogin();

window.onload = function () {

    loadDashboard();

};

// -------------------------------
// Dashboard Stats
// -------------------------------

async function loadDashboard() {

    try {

        showLoader();

        const data = await apiGet("/dashboard/stats");

        hideLoader();

        // Cards

        document.getElementById("totalBooks").innerText =
            data.total_books ?? 0;

        document.getElementById("availableCopies").innerText =
            data.available_copies ?? 0;

        document.getElementById("borrowedBooks").innerText =
            data.borrowed_books ?? 0;

        document.getElementById("reservationCount").innerText =
            data.total_reservations ?? 0;

        document.getElementById("pendingReservations").innerText =
            data.pending_reservations ?? 0;

        document.getElementById("wishlistCount").innerText =
            data.total_wishlist ?? 0;

        document.getElementById("popularBook").innerText =
            data.popular_book ?? "N/A";

        document.getElementById("activeUser").innerText =
            data.active_user ?? "N/A";

        loadRecentBooks(data.recent_books);

        loadActivity(data.recent_activity);

    }

    catch (err) {

        hideLoader();

        console.error(err);

        showToast(err.message, "error");

    }

}

// -------------------------------
// Recent Books
// -------------------------------

function loadRecentBooks(books) {

    const table = document.getElementById("recentBooks");

    table.innerHTML = "";

    if (!books || books.length === 0) {

        table.innerHTML =

        `<tr>

            <td colspan="4">

                No Books Found

            </td>

        </tr>`;

        return;

    }

    books.forEach(book => {

        table.innerHTML += `

        <tr>

            <td>${book.title}</td>

            <td>${book.author}</td>

            <td>${book.subject}</td>

            <td>${book.availability}</td>

        </tr>

        `;

    });

}

// -------------------------------
// Recent Activity
// -------------------------------

function loadActivity(activity) {

    const table = document.getElementById("activityTable");

    table.innerHTML = "";

    if (!activity || activity.length === 0) {

        table.innerHTML =

        `<tr>

            <td colspan="3">

                No Recent Activity

            </td>

        </tr>`;

        return;

    }

    activity.forEach(item => {

        table.innerHTML += `

        <tr>

            <td>${item.time}</td>

            <td>${item.user}</td>

            <td>${item.action}</td>

        </tr>

        `;

    });

}