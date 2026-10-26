/* GTA VI Countdown von Leonida News Network (https://leonida-news.de/countdown.html)
   Einbau: <div class="lnn-countdown" data-theme="dark"></div><script src="https://leonida-news.de/widget/gta6-countdown.js" async></script>
   Kein Tracking, keine Cookies, keine weiteren Anfragen. */
(function () {
  var RELEASE = Date.parse('2026-11-19T00:00:00+01:00');
  var CSS =
    ':host{all:initial;display:block}' +
    '.box{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;border-radius:10px;padding:14px 16px 12px;max-width:420px;box-sizing:border-box;text-align:center;line-height:1.2}' +
    '.dark{background:#07070c;color:#f4f2f7;border:1px solid #262636}' +
    '.light{background:#fff;color:#221c18;border:1px solid #e5e0d6}' +
    '.k{display:inline-block;background:#e11d48;color:#fff;font-weight:800;font-size:11px;letter-spacing:.14em;text-transform:uppercase;padding:4px 8px;border-radius:3px}' +
    '.t{font-weight:900;font-size:20px;letter-spacing:.02em;margin:8px 0 10px;text-transform:uppercase}' +
    '.g{display:flex;gap:8px;justify-content:center}' +
    '.c{flex:1;min-width:0;border-radius:8px;padding:8px 2px 6px}' +
    '.dark .c{background:#10101a}.light .c{background:#f5f1e8}' +
    '.n{display:block;font-weight:900;font-size:28px;font-variant-numeric:tabular-nums}' +
    '.l{display:block;font-size:11px;opacity:.7;margin-top:2px}' +
    '.done{font-weight:900;font-size:26px;color:#fbbf24;margin:6px 0 4px;text-transform:uppercase}' +
    '.f{margin-top:10px;font-size:12px;opacity:.85}' +
    '.f a{color:inherit;font-weight:700;text-decoration:none}' +
    '.dark .f a b{color:#fbbf24}.light .f a b{color:#e11d48}' +
    '.f a:hover{text-decoration:underline}';
  var LABELS = ['Tage', 'Std', 'Min', 'Sek'];

  function pad(n) { return (n < 10 ? '0' : '') + n; }

  function mount(el) {
    if (el.__lnn) return;
    el.__lnn = true;
    var theme = el.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
    var root = el.attachShadow ? el.attachShadow({ mode: 'open' }) : el;
    var style = document.createElement('style');
    style.textContent = CSS;
    var box = document.createElement('div');
    box.className = 'box ' + theme;
    box.innerHTML =
      '<span class="k">GTA VI</span>' +
      '<div class="t">Release am 19. November</div>' +
      '<div class="g" aria-live="off"></div>' +
      '<div class="f">Alle News mit Quelle: <a href="https://leonida-news.de/" target="_blank" rel="noopener">leonida-news<b>.de</b></a></div>';
    root.appendChild(style);
    root.appendChild(box);
    var grid = box.querySelector('.g');
    var cells = [];
    for (var i = 0; i < 4; i++) {
      var c = document.createElement('div');
      c.className = 'c';
      c.innerHTML = '<span class="n">0</span><span class="l">' + LABELS[i] + '</span>';
      grid.appendChild(c);
      cells.push(c.firstChild);
    }
    function tick() {
      var s = Math.floor((RELEASE - Date.now()) / 1000);
      if (s <= 0) {
        grid.outerHTML = '<div class="done">Jetzt erhältlich</div>';
        clearInterval(timer);
        return;
      }
      var v = [Math.floor(s / 86400), Math.floor(s % 86400 / 3600), Math.floor(s % 3600 / 60), s % 60];
      cells[0].textContent = v[0];
      for (var j = 1; j < 4; j++) cells[j].textContent = pad(v[j]);
    }
    var timer = setInterval(tick, 1000);
    tick();
  }

  function run() {
    var els = document.querySelectorAll('.lnn-countdown');
    for (var i = 0; i < els.length; i++) mount(els[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
})();
