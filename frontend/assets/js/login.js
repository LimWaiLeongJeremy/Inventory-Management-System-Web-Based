// ========== Config ==========
const API_BASE_URL = ""; 
const TOKEN_KEY = "access_token";

//  Elements 
const form = document.getElementById("loginForm");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const rememberInput = document.getElementById("remember");
const toggleBtn = document.getElementById("togglePassword");
const eyeIcon = toggleBtn.querySelector("img");
const loginBtn = document.getElementById("loginBtn");
const btnLabel = loginBtn.querySelector("span");
const message = document.getElementById("formMessage");


// Helpers 
function showMessage(text, type = "error") {
  message.textContent = text;
  message.classList.toggle("info", type === "info");
  message.hidden = false;
}

function clearMessage() {
  message.hidden = true;
  message.textContent = "";
  usernameInput.removeAttribute("aria-invalid");
  passwordInput.removeAttribute("aria-invalid");
}

function setLoading(isLoading) {
  loginBtn.disabled = isLoading;
  btnLabel.textContent = isLoading ? "Logging in…" : "Log in";
}

// keep token after the browser closes, otherwise only for this tab
function saveToken(token, remember) {
  localStorage.removeItem(TOKEN_KEY);
  sessionStorage.removeItem(TOKEN_KEY);
  (remember ? localStorage : sessionStorage).setItem(TOKEN_KEY, token);
}


//Show / hide password
toggleBtn.addEventListener("click", () => {
  const isHidden = passwordInput.type === "password";
  passwordInput.type = isHidden ? "text" : "password";
  eyeIcon.src = isHidden ? "assets/icons/eye-off.svg" : "assets/icons/eye.svg";
  toggleBtn.setAttribute("aria-label", isHidden ? "Hide password" : "Show password");
});


// Help links
document.getElementById("forgotLink").addEventListener("click", (e) => {
  e.preventDefault();
  showMessage("Please contact your workspace administrator to reset your password.", "info");
});

document.getElementById("contactLink").addEventListener("click", (e) => {
  e.preventDefault();
  showMessage("Please contact your workspace administrator for help logging in.", "info");
});


// Login
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  clearMessage();

  const username = usernameInput.value.trim();
  const password = passwordInput.value;

  // validate input (same rules as the API)
  if (!username) {
    usernameInput.setAttribute("aria-invalid", "true");
    usernameInput.focus();
    return showMessage("Username cannot be empty");
  }

  if (!password) {
    passwordInput.setAttribute("aria-invalid", "true");
    passwordInput.focus();
    return showMessage("Password cannot be empty");
  }

  setLoading(true);

  try {
    const response = await fetch(`${API_BASE_URL}/api/user/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    const result = await response.json().catch(() => ({}));

    if (!response.ok || result.status !== "success") {
      passwordInput.value = "";
      passwordInput.focus();
      return showMessage(result.data || "Login failed. Please try again.");
    }

    saveToken(result.token, rememberInput.checked);
    showMessage("Logged in successfully.", "info");

  } catch (err) {
    console.error(err);
    showMessage("Cannot reach the server. Please check that the backend is running.");
  } finally {
    setLoading(false);
  }
});
