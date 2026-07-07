// ===============================
// ShelfShare API Configuration
// ===============================

const API_BASE = "https://shelfshare-api.onrender.com";

// ===============================
// JWT Token
// ===============================

function getToken() {
    return localStorage.getItem("token");
}

function saveToken(token) {
    localStorage.setItem("token", token);
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

// ===============================
// Common Headers
// ===============================

function getHeaders() {

    const headers = {
        "Content-Type": "application/json"
    };

    const token = getToken();

    if (token) {
        headers["Authorization"] = "Bearer " + token;
    }

    return headers;
}

// ===============================
// GET Request
// ===============================

async function apiGet(endpoint) {

    const response = await fetch(
        API_BASE + endpoint,
        {
            method: "GET",
            headers: getHeaders()
        }
    );

    return handleResponse(response);

}

// ===============================
// POST Request
// ===============================

async function apiPost(endpoint, data) {

    const response = await fetch(
        API_BASE + endpoint,
        {
            method: "POST",

            headers: getHeaders(),

            body: JSON.stringify(data)
        }
    );

    return handleResponse(response);

}

// ===============================
// PUT Request
// ===============================

async function apiPut(endpoint, data) {

    const response = await fetch(
        API_BASE + endpoint,
        {
            method: "PUT",

            headers: getHeaders(),

            body: JSON.stringify(data)
        }
    );

    return handleResponse(response);

}

// ===============================
// DELETE Request
// ===============================

async function apiDelete(endpoint) {

    const response = await fetch(
        API_BASE + endpoint,
        {
            method: "DELETE",

            headers: getHeaders()
        }
    );

    return handleResponse(response);

}

// ===============================
// Response Handler
// ===============================

async function handleResponse(response) {

    if (!response.ok) {

        let error;

        try {

            error = await response.json();

        } catch {

            throw new Error("Server Error");

        }

        throw new Error(
            error.detail || "Request Failed"
        );

    }

    if (response.status === 204) {

        return null;

    }

    return await response.json();

}

// ===============================
// Toast Notification
// ===============================

function showToast(message, type = "success") {

    let toast = document.getElementById("toast");

    if (!toast) {

        toast = document.createElement("div");

        toast.id = "toast";

        toast.className = "toast";

        document.body.appendChild(toast);

    }

    toast.className = "toast show " + type;

    toast.innerText = message;

    setTimeout(() => {

        toast.className = "toast";

    }, 3000);

}

// ===============================
// Loading Spinner
// ===============================

function showLoader() {

    const loader = document.getElementById("loader");

    if (loader) {

        loader.classList.remove("hidden");

    }

}

function hideLoader() {

    const loader = document.getElementById("loader");

    if (loader) {

        loader.classList.add("hidden");

    }

}