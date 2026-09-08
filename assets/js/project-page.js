(function () {
    "use strict";

    function splitValues(element, name) {
        return (element.getAttribute("data-" + name) || "").split("|");
    }

    function initializeSnrExplorer() {
        var explorer = document.querySelector("[data-snr-explorer]");
        if (!explorer) return;

        var input = explorer.querySelector('input[type="range"]');
        var labels = splitValues(input, "labels");
        var sim = splitValues(input, "sim");
        var protection = splitValues(input, "protection");
        var stoi = splitValues(input, "stoi");
        var wer = splitValues(input, "wer");

        function update() {
            var index = Number(input.value);
            explorer.querySelector("[data-snr-label]").textContent = labels[index];
            explorer.querySelector("[data-snr-sim]").textContent = sim[index];
            explorer.querySelector("[data-snr-protection]").textContent = protection[index] + "%";
            explorer.querySelector("[data-snr-stoi]").textContent = stoi[index];
            explorer.querySelector("[data-snr-wer]").textContent = wer[index] + "%";
        }

        input.addEventListener("input", update);
        update();
    }

    function initializeRobustnessExplorer() {
        var explorer = document.querySelector("[data-robustness-explorer]");
        if (!explorer) return;

        var buttons = explorer.querySelectorAll("[data-sim]");
        var label = explorer.querySelector("[data-robustness-label]");
        var simValue = explorer.querySelector("[data-robustness-sim]");
        var bar = explorer.querySelector("[data-robustness-bar]");

        buttons.forEach(function (button) {
            button.addEventListener("click", function () {
                buttons.forEach(function (item) {
                    item.classList.remove("active");
                    item.setAttribute("aria-pressed", "false");
                });
                button.classList.add("active");
                button.setAttribute("aria-pressed", "true");

                var sim = Number(button.getAttribute("data-sim"));
                label.textContent = button.getAttribute("data-label");
                simValue.textContent = sim.toFixed(3);
                bar.style.width = (sim * 100).toFixed(1) + "%";
            });
        });

        buttons.forEach(function (button, index) {
            button.setAttribute("aria-pressed", index === 0 ? "true" : "false");
        });
    }

    function preventSimultaneousAudio() {
        document.querySelectorAll("audio").forEach(function (audio) {
            audio.addEventListener("play", function () {
                document.querySelectorAll("audio").forEach(function (other) {
                    if (other !== audio) other.pause();
                });
            });
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        initializeSnrExplorer();
        initializeRobustnessExplorer();
        preventSimultaneousAudio();
    });
})();
