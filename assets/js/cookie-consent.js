(function() {
  var COOKIE_KEY = 'muchotexto_cookie_consent';

  function getConsent() {
    return localStorage.getItem(COOKIE_KEY);
  }

  function setConsent(value) {
    localStorage.setItem(COOKIE_KEY, value);
  }

  function hideBanner() {
    var banner = document.getElementById('cookie-banner');
    if (banner) banner.style.display = 'none';
  }

  function loadGA() {
    if (window.gtag) return;
    var script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=G-LLZE5F9CB7';
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', 'G-LLZE5F9CB7');
  }

  var consent = getConsent();

  if (consent === 'accepted') {
    hideBanner();
    loadGA();
  } else if (consent === 'rejected') {
    hideBanner();
  } else {
    document.addEventListener('DOMContentLoaded', function() {
      var banner = document.getElementById('cookie-banner');
      if (banner) banner.style.display = 'block';

      document.getElementById('cookie-accept').addEventListener('click', function() {
        setConsent('accepted');
        hideBanner();
        loadGA();
      });

      document.getElementById('cookie-reject').addEventListener('click', function() {
        setConsent('rejected');
        hideBanner();
      });
    });
  }
})();
