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
        preventSimultaneousAudio();
    });
})();
