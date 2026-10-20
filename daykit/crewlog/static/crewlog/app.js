const searchInput = document.querySelector(".search input");

if (searchInput) {
    searchInput.addEventListener("input", () => {
        searchInput.dataset.hasText = searchInput.value.trim() ? "true" : "false";
    });
}

const clock = document.querySelector("[data-clock]");

function updateClock() {
    if (!clock) {
        return;
    }

    const now = new Date();
    clock.textContent = now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
    });
}

updateClock();
setInterval(updateClock, 30000);
