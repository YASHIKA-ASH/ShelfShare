checkLogin();

async function loadReservations() {

    const userId = document.getElementById("reservationUser").value;

    if (!userId) {

        showToast("Enter User ID", "error");

        return;

    }

    try {

        showLoader();

        const reservations = await apiGet(`/reservations/${userId}`);

        hideLoader();

        renderReservations(reservations);

    }

    catch (err) {

        hideLoader();

        showToast(err.message, "error");

    }

}

function renderReservations(data) {

    const list = document.getElementById("reservationList");

    list.innerHTML = "";

    if (!data || data.length === 0) {

        list.innerHTML = "<h3>No Reservations</h3>";

        return;

    }

    data.forEach(item => {

        list.innerHTML += `

        <div class="reservation-card">

            <h2>${item.title}</h2>

            <p><b>Author:</b> ${item.author}</p>

            <p><b>Queue Position:</b> ${item.position}</p>

            <p><b>Status:</b> ${item.status}</p>

            <button
                class="primary-btn"
                onclick="cancelReservation(${item.id})">

                Cancel Reservation

            </button>

        </div>

        `;

    });

}

async function cancelReservation(id) {

    if (!confirm("Cancel Reservation?")) {

        return;

    }

    try {

        await apiDelete(`/reservations/${id}`);

        showToast("Reservation Cancelled");

        loadReservations();

    }

    catch (err) {

        showToast(err.message, "error");

    }

}

window.onload = function () {

    const user = localStorage.getItem("user_id");

    if (user) {

        document.getElementById("reservationUser").value = user;

        loadReservations();

    }

};