/* BigCatWise games: shared helpers. Original code (c) 2026 Joshua Israel Ventures LLC.
   No network requests, no tracking. Best scores stay in this browser only (localStorage). */
(function () {
  "use strict";
  var BCW = {};
  BCW.reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- best score, local only ---- */
  BCW.getBest = function (key) {
    try { var v = window.localStorage.getItem(key); return v === null ? null : Number(v); } catch (e) { return null; }
  };
  BCW.setBest = function (key, val) {
    try { window.localStorage.setItem(key, String(val)); } catch (e) { /* storage blocked: ignore */ }
  };

  /* ---- sound: off by default, tiny synthesised beeps, no audio files ---- */
  var ctx = null, soundOn = false;
  BCW.beep = function (freq, ms, type) {
    if (!soundOn) return;
    try {
      ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
      var o = ctx.createOscillator(), g = ctx.createGain();
      o.type = type || "sine"; o.frequency.value = freq;
      g.gain.setValueAtTime(0.08, ctx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + ms / 1000);
      o.connect(g); g.connect(ctx.destination); o.start(); o.stop(ctx.currentTime + ms / 1000);
    } catch (e) { /* no audio support */ }
  };
  BCW.good = function () { BCW.beep(660, 140); setTimeout(function () { BCW.beep(880, 160); }, 120); };
  BCW.bad = function () { BCW.beep(200, 220, "triangle"); };
  BCW.initSound = function (btn) {
    if (!btn) return;
    btn.setAttribute("aria-pressed", "false");
    btn.addEventListener("click", function () {
      soundOn = !soundOn;
      btn.setAttribute("aria-pressed", soundOn ? "true" : "false");
      btn.textContent = soundOn ? "Sound: on" : "Sound: off";
      if (soundOn) BCW.beep(520, 90);
    });
  };

  /* ---- original cartoon cat faces, drawn as inline SVG ---- */
  var C = {
    lion: { fur: "#d9a55b", ear: "#b9803a", mark: "none" },
    tiger: { fur: "#f08a24", ear: "#c4621a", mark: "stripes" },
    leopard: { fur: "#f0bf5a", ear: "#c9923a", mark: "rosettes" },
    jaguar: { fur: "#e8a845", ear: "#b9782a", mark: "dots" },
    cheetah: { fur: "#f2c766", ear: "#c99b3c", mark: "tears" },
    snow: { fur: "#dcd8cf", ear: "#a9a49a", mark: "grey" }
  };
  BCW.NAMES = { lion: "Lion", tiger: "Tiger", leopard: "Leopard", jaguar: "Jaguar", cheetah: "Cheetah", snow: "Snow leopard" };
  BCW.ORDER = ["lion", "tiger", "leopard", "jaguar", "cheetah", "snow"];
  BCW.face = function (sp, size) {
    var c = C[sp], s = size || 64, k = "#2a1d12", m = "";
    if (sp === "lion") m = '<circle cx="32" cy="36" r="27" fill="#a8652a"/><circle cx="32" cy="36" r="27" fill="none" stroke="#8a4f1c" stroke-width="3" stroke-dasharray="5 4"/>';
    var marks = "";
    if (c.mark === "stripes") marks = '<path d="M32 15v7M24 17l2 6M40 17l-2 6M13 34h7M44 34h7M14 41l6-1M50 41l-6-1" stroke="' + k + '" stroke-width="2.6" stroke-linecap="round"/>';
    if (c.mark === "rosettes") marks = '<circle cx="22" cy="21" r="1.8" fill="' + k + '"/><circle cx="42" cy="21" r="1.8" fill="' + k + '"/><circle cx="32" cy="18" r="1.8" fill="' + k + '"/><circle cx="17" cy="38" r="1.6" fill="' + k + '"/><circle cx="47" cy="38" r="1.6" fill="' + k + '"/>';
    if (c.mark === "dots") marks = '<circle cx="22" cy="21" r="3.2" fill="none" stroke="' + k + '" stroke-width="1.8"/><circle cx="22" cy="21" r=".9" fill="' + k + '"/><circle cx="42" cy="21" r="3.2" fill="none" stroke="' + k + '" stroke-width="1.8"/><circle cx="42" cy="21" r=".9" fill="' + k + '"/>';
    if (c.mark === "tears") marks = '<path d="M24 31q-3 7 0 13M40 31q3 7 0 13" stroke="' + k + '" stroke-width="2.4" fill="none" stroke-linecap="round"/><circle cx="20" cy="20" r="1.6" fill="' + k + '"/><circle cx="44" cy="20" r="1.6" fill="' + k + '"/>';
    if (c.mark === "grey") marks = '<circle cx="21" cy="20" r="3" fill="none" stroke="#5d5850" stroke-width="1.8"/><circle cx="43" cy="20" r="3" fill="none" stroke="#5d5850" stroke-width="1.8"/>';
    var eye = sp === "snow" ? "#7d8f8a" : k;
    return '<svg class="face" width="' + s + '" height="' + s + '" viewBox="0 0 64 64" aria-hidden="true" focusable="false">' + m +
      '<path d="M12 22 L14 6 L26 16Z M52 22 L50 6 L38 16Z" fill="' + c.ear + '"/>' +
      (sp === "tiger" ? '<circle cx="15" cy="11" r="2.4" fill="#fff"/><circle cx="49" cy="11" r="2.4" fill="#fff"/>' : "") +
      '<ellipse cx="32" cy="34" rx="22" ry="20" fill="' + c.fur + '"/>' +
      '<ellipse cx="32" cy="43" rx="10" ry="7" fill="#fff7ea"/>' + marks +
      '<circle cx="24" cy="30" r="3.2" fill="' + eye + '"/><circle cx="40" cy="30" r="3.2" fill="' + eye + '"/>' +
      '<circle cx="25" cy="29" r="1" fill="#fff"/><circle cx="41" cy="29" r="1" fill="#fff"/>' +
      '<path d="M29 39h6l-3 3z" fill="#e2747a"/><path d="M32 42v2M32 44q-3 2-5 0M32 44q3 2 5 0" stroke="' + k + '" stroke-width="1.4" fill="none" stroke-linecap="round"/></svg>';
  };

  BCW.shuffle = function (a) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  };
  window.BCW = BCW;
})();
