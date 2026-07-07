// ======================================
// ShelfShare Authentication
// ======================================

// ---------- Register ----------

async function registerUser() {

    const full_name = document.getElementById("fullName").value.trim();

    const email = document.getElementById("registerEmail").value.trim();

    const password = document.getElementById("registerPassword").value.trim();

    const phone = document.getElementById("phone").value.trim();

    const role = document.getElementById("role").value;

    if (!full_name || !email || !password) {

        showToast("Please fill all required fields", "error");

        return;

    }

    try {

        showLoader();

        const response = await apiPost("/users/register", {

            full_name: full_name,

            email: email,

            password: password,

            phone: phone,

            role: role

        });

        hideLoader();

        showToast("Registration Successful");

        showLogin();

    }

    catch (err) {

        hideLoader();

        showToast(err.message, "error");

    }

}

// ---------- Login ----------

async function login() {

    const email = document.getElementById("loginEmail").value.trim();

    const password = document.getElementById("loginPassword").value.trim();

    if (!email || !password) {

        showToast("Enter Email & Password", "error");

        return;

    }

    try {

        showLoader();

        const response = await apiPost("/users/login", {

            email: email,

            password: password

        });

        hideLoader();

        saveToken(response.access_token);

        showToast("Login Successful");

        setTimeout(() => {

            window.location.href = "dashboard.html";

        }, 800);

    }

    catch (err) {

        hideLoader();

        showToast(err.message, "error");

    }

}

// ---------- Logout ----------

function performLogout() {

    logout();

}

// ---------- Check Login ----------

function checkLogin() {

    const token = getToken();

    if (!token) {

        window.location.href = "index.html";

    }

}

// ---------- Auto Redirect ----------

(function () {

    const page = window.location.pathname;

    if (page.includes("dashboard") ||

        page.includes("books") ||

        page.includes("borrow") ||

        page.includes("inventory") ||

        page.includes("wishlist") ||

        page.includes("reservation") ||

        page.includes("scan")) {

        checkLogin();

    }

})();