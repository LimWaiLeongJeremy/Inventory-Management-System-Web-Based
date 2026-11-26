// Config
const TOKEN_KEY = "access_token";   // same key as login.js
const LOGIN_URL = "/login";

// Elements
const sidebar = document.getElementById("sidebar");
const navToggle = document.getElementById("navToggle");
const backdrop = document.getElementById("navBackdrop");
const userBtn = document.getElementById("userBtn");
const userMenu = document.getElementById("userMenu");
const logoutBtn = document.getElementById("logoutBtn");




// Open / close the sidebar on small screens
function setNavOpen(isOpen) {
  sidebar.classList.toggle("open", isOpen);
  backdrop.hidden = !isOpen;
  navToggle.setAttribute("aria-expanded", String(isOpen));
  navToggle.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
}

navToggle.addEventListener("click", () => setNavOpen(!sidebar.classList.contains("open")));
backdrop.addEventListener("click", () => setNavOpen(false));

document.addEventListener("keydown", (e) => {
  if (e.key !== "Escape") return;

  // Close the user menu first, then the sidebar
  if (!userMenu.hidden) {
    setUserMenuOpen(false);
    userBtn.focus();
  } else if (sidebar.classList.contains("open")) {
    setNavOpen(false);
    navToggle.focus();
  }
});


// User menu (opens above the username / role button)
function setUserMenuOpen(isOpen) {
  userMenu.hidden = !isOpen;
  userBtn.setAttribute("aria-expanded", String(isOpen));
}

userBtn.addEventListener("click", () => {
  const willOpen = userMenu.hidden;
  setUserMenuOpen(willOpen);
  if (willOpen) logoutBtn.focus();
});

// Close the menu when clicking anywhere else
document.addEventListener("click", (e) => {
  if (!userMenu.hidden && !userMenu.contains(e.target) && !userBtn.contains(e.target)) {
    setUserMenuOpen(false);
  }
});


// Log out: end the server session, forget the API token, go back to login
logoutBtn.addEventListener("click", async () => {
  logoutBtn.disabled = true;

  try {
    await fetch("/api/user/logout", { method: "POST" });
  } catch (err) {
    // Still leave the page; the session check on /dashboard will send them to login if needed
    console.error(err);
  }

  localStorage.removeItem(TOKEN_KEY);
  sessionStorage.removeItem(TOKEN_KEY);

  // replace() so the back button does not return to the dashboard
  window.location.replace(LOGIN_URL);
});
