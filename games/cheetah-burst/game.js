/* Cheetah Burst: original code and art (c) 2026 Joshua Israel Ventures LLC. */
(function () {
  "use strict";
  var B = window.BCW, root = document.getElementById("cb");
  if (!B || !root) return;
  var BEST = "bcwCheetahBurstBest";
  /* Real figures used in the game, all published on BigCatWise (how-fast-is-a-cheetah.html):
     fastest run measured in wild cheetahs 25.9 m/s (about 93 km/h); chases seldom more than about 300 m. */
  var TOP = 25.9, LIMIT = 300;
  var FACTS = [
    "The fastest run measured in wild hunting cheetahs was 25.9 metres per second, about 93 km/h (58 mph), recorded with GPS collars in Botswana (Wilson et al., 2013, Nature).",
    "In the same study, the average top speed of a run was only 14.9 m/s, about 54 km/h. Wild cheetahs rarely run flat out.",
    "Cheetah chases seldom cover more than about 300 m, according to the IUCN Cat Specialist Group.",
    "Successful hunts in the Botswana study involved hard braking and sharp turns as the prey dodged. Agility mattered as much as top speed.",
    "Cheetahs do not give up chases because they overheat: body temperature measured in free living cheetahs did not rise enough during hunts to explain stopping (Hetem et al., 2013, Biology Letters).",
    "A cheetah's stride can reach about 7 m, helped by a flexible spine that flexes and extends with each bound.",
    "Semi retractable claws stay partly out, gripping the ground like running shoe spikes when the cheetah accelerates and turns.",
    "A cheetah's long tail, about half its head and body length, helps it balance and steer in turns."
  ];
  var el = function (id) { return root.querySelector("#" + id); };
  var stage = el("cb-stage"), cat = el("cb-cat"), prey = el("cb-prey"), ground = el("cb-ground"), speedTxt = el("cb-speed"), distTxt = el("cb-dist"),
      energyBar = el("cb-energy"), runBtn = el("cb-run"), turnBtn = el("cb-turn"), startBtn = el("cb-start"), msg = el("cb-msg"), fact = el("cb-fact"), live = el("cb-live"), swerveCue = el("cb-swerve");
  B.initSound(el("cb-sound"));
  var best = B.getBest(BEST);
  function showBest() { el("cb-best").textContent = best === null ? "none yet" : best.toFixed(1) + " s"; }
  showBest();
  var st = null, raf = 0, factIdx = Math.floor(Math.random() * FACTS.length);

  function reset() {
    st = { v: 0, dist: 0, gap: 30, pv: 14, energy: 100, t: 0, swerveAt: 1.6 + Math.random(), swerveOpen: 0, running: true, last: 0, turns: 0 };
  }
  function tap() {
    if (!st || !st.running) return;
    if (st.energy <= 0) return;
    st.v = Math.min(TOP, st.v + 2.1);
    B.beep(300 + st.v * 18, 40);
    cat.classList.add("bound"); setTimeout(function () { cat.classList.remove("bound"); }, 90);
  }
  function turn() {
    if (!st || !st.running) return;
    if (st.swerveOpen > 0) { st.swerveOpen = 0; st.turns++; swerveCue.hidden = true; B.good(); live.textContent = "Nice turn!"; }
    else { st.v *= 0.85; B.bad(); }
  }
  function frame(now) {
    if (!st || !st.running) return;
    var dt = st.last ? Math.min(0.05, (now - st.last) / 1000) : 0; st.last = now; st.t += dt;
    st.v = Math.max(0, st.v - 2.6 * dt);
    st.energy = Math.max(0, st.energy - (3 + 20 * Math.pow(st.v / TOP, 2)) * dt);
    if (st.energy <= 0) st.v = Math.max(0, st.v - 9 * dt);
    st.pv = 14 + 2 * Math.sin(st.t * 1.3);
    st.t >= st.swerveAt && st.swerveOpen <= 0 && (st.swerveOpen = 0.9, st.swerveAt = st.t + 1.7 + Math.random() * 1.2, swerveCue.hidden = false, live.textContent = "The prey swerves! Turn now!", B.beep(990, 70, "square"));
    if (st.swerveOpen > 0) {
      st.swerveOpen -= dt;
      if (st.swerveOpen <= 0) { st.v *= 0.45; st.gap += 4; swerveCue.hidden = true; live.textContent = "Missed the turn. You overshot!"; B.bad(); }
    }
    st.dist += st.v * dt; st.gap += (st.pv - st.v) * dt;
    var kmh = st.v * 3.6;
    speedTxt.textContent = kmh.toFixed(0) + " km/h"; distTxt.textContent = st.dist.toFixed(0) + " m of " + LIMIT + " m";
    energyBar.style.width = st.energy.toFixed(0) + "%";
    var w = stage.clientWidth, px = Math.max(0, Math.min(1, st.gap / 60));
    prey.style.transform = "translateX(" + (px * (w * 0.62)).toFixed(0) + "px)" + (st.swerveOpen > 0 ? " translateY(-10px)" : "");
    if (!B.reduced) ground.style.backgroundPositionX = (-st.dist * 12).toFixed(0) + "px";
    if (st.gap <= 0) return end(true, "Caught it in " + st.t.toFixed(1) + " s after " + st.dist.toFixed(0) + " m!");
    if (st.dist >= LIMIT) return end(false, "The prey got away. Real cheetah chases seldom go past about 300 m.");
    if (st.energy <= 0 && st.v < 0.5) return end(false, "Out of puff! Sprinting at top speed burns energy fast.");
    if (st.gap > 70) return end(false, "The prey got too far ahead.");
    raf = requestAnimationFrame(frame);
  }
  function end(win, text) {
    st.running = false; cancelAnimationFrame(raf); swerveCue.hidden = true;
    var line = text;
    if (win) { B.good(); if (best === null || st.t < best) { best = Math.round(st.t * 10) / 10; B.setBest(BEST, best); line += " New best time!"; } }
    else B.bad();
    showBest();
    msg.textContent = line; live.textContent = line;
    fact.innerHTML = '<div class="factface">' + B.face("cheetah", 64) + '</div><p><b>Cheetah fact:</b> ' + FACTS[factIdx] + '</p>';
    factIdx = (factIdx + 1) % FACTS.length; fact.hidden = false;
    runBtn.disabled = true; turnBtn.disabled = true;
    startBtn.textContent = "Chase again"; startBtn.hidden = false; startBtn.focus({ preventScroll: true });
  }
  function start() {
    reset(); msg.textContent = "Go! Tap Sprint fast. Hit Turn when the prey swerves."; fact.hidden = true;
    runBtn.disabled = false; turnBtn.disabled = false; startBtn.hidden = true; runBtn.focus({ preventScroll: true });
    cancelAnimationFrame(raf); raf = requestAnimationFrame(frame);
  }
  startBtn.addEventListener("click", start);
  runBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); tap(); });
  runBtn.addEventListener("click", function (e) { if (e.detail === 0) tap(); }); /* keyboard activation */
  turnBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); turn(); });
  turnBtn.addEventListener("click", function (e) { if (e.detail === 0) turn(); });
  document.addEventListener("keydown", function (e) {
    if (!st || !st.running || e.repeat) return;
    if (e.code === "Space" || e.key === "ArrowRight") { e.preventDefault(); tap(); }
    else if (e.key === "ArrowUp" || e.key === "ArrowDown" || e.key === "t" || e.key === "T") { e.preventDefault(); turn(); }
  });
})();
