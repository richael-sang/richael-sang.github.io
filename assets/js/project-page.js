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

    function currentLanguage() {
        var lang = document.documentElement.getAttribute("data-sceneguard-lang");
        return lang === "zh" ? "zh" : "en";
    }

    function applyLanguage(lang) {
        var resolved = lang === "zh" ? "zh" : "en";
        document.documentElement.setAttribute("data-sceneguard-lang", resolved);
        document.documentElement.lang = resolved === "zh" ? "zh-CN" : "en";

        document.querySelectorAll(".project-lang-switch button").forEach(function (button) {
            button.setAttribute("aria-pressed", button.getAttribute("data-lang") === resolved ? "true" : "false");
        });

        document.querySelectorAll("[data-alt-en][data-alt-zh]").forEach(function (image) {
            image.setAttribute("alt", image.getAttribute("data-alt-" + resolved));
        });

        try {
            window.localStorage.setItem("sceneguard-lang", resolved);
        } catch (error) {}
    }

    function initializeLanguageSwitch() {
        var switches = document.querySelectorAll(".project-lang-switch button");
        if (!switches.length) return;

        switches.forEach(function (button) {
            button.addEventListener("click", function () {
                applyLanguage(button.getAttribute("data-lang"));
            });
        });

        applyLanguage(currentLanguage());
    }

    document.addEventListener("DOMContentLoaded", function () {
        initializeLanguageSwitch();
        initializeSnrExplorer();
        preventSimultaneousAudio();
    });
})();
