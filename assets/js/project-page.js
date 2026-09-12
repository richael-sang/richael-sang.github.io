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

    function initializeRgbirDemo() {
        var root = document.querySelector("[data-rgbir-demo]");
        if (!root) return;

        var payload = root.getAttribute("data-rgbir-demo");
        if (!payload) return;

        var cases;
        try {
            cases = JSON.parse(payload);
        } catch (error) {
            return;
        }

        var buttons = root.querySelectorAll("[data-rgbir-case]");
        var panes = root.querySelectorAll("[data-rgbir-pane]");
        var note = root.querySelector("[data-rgbir-note]");

        function render(name) {
            var selected = cases[name] || {};
            buttons.forEach(function (button) {
                button.setAttribute("aria-pressed", button.getAttribute("data-rgbir-case") === name ? "true" : "false");
            });
            panes.forEach(function (pane) {
                var key = pane.getAttribute("data-rgbir-pane");
                var item = selected[key] || {};
                var image = pane.querySelector("img");
                var empty = pane.querySelector("[data-empty]");
                var caption = pane.querySelector("[data-caption]");
                var stats = pane.querySelector("[data-stats]");
                if (item.src) {
                    image.hidden = false;
                    image.src = item.src;
                    image.alt = item.alt || "";
                    if (empty) empty.hidden = true;
                } else {
                    image.removeAttribute("src");
                    image.hidden = true;
                    if (empty) {
                        empty.hidden = false;
                        empty.textContent = item.empty || "No verified image available.";
                    }
                }
                if (caption) caption.textContent = item.caption || "";
                if (stats) {
                    if (item.tp != null || item.fn != null || item.fp != null) {
                        var parts = [];
                        if (item.tp != null) parts.push("TP " + item.tp);
                        if (item.fp != null) parts.push("FP " + item.fp);
                        if (item.fn != null) parts.push("FN " + item.fn);
                        stats.hidden = false;
                        stats.textContent = parts.join(" · ");
                    } else {
                        stats.hidden = true;
                        stats.textContent = "";
                    }
                }
            });
            if (note) note.textContent = selected.note || "";
        }

        buttons.forEach(function (button) {
            button.addEventListener("click", function () {
                render(button.getAttribute("data-rgbir-case"));
            });
        });

        var initial = root.getAttribute("data-rgbir-initial") || buttons[0].getAttribute("data-rgbir-case");
        render(initial);
    }

    document.addEventListener("DOMContentLoaded", function () {
        initializeLanguageSwitch();
        initializeSnrExplorer();
        initializeRgbirDemo();
        preventSimultaneousAudio();
    });
})();
