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

  function updateGAConsent(granted) {
    if (typeof gtag !== 'function') return;
    gtag('consent', 'update', {
      'analytics_storage': granted ? 'granted' : 'denied'
    });
  }

  var consent = getConsent();

  if (consent === 'accepted') {
    hideBanner();
    updateGAConsent(true);
  } else if (consent === 'rejected') {
    hideBanner();
    updateGAConsent(false);
  } else {
    document.addEventListener('DOMContentLoaded', function() {
      var banner = document.getElementById('cookie-banner');
      if (banner) banner.style.display = 'block';

      document.getElementById('cookie-accept').addEventListener('click', function() {
        setConsent('accepted');
        hideBanner();
        updateGAConsent(true);
      });

      document.getElementById('cookie-reject').addEventListener('click', function() {
        setConsent('rejected');
        hideBanner();
        updateGAConsent(false);
      });
    });
  }
})();
