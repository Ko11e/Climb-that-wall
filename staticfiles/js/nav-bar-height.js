document.addEventListener("DOMContentLoaded", function() {
    if (document.getElementById("height-not-fixed")) {
      let div = document.getElementById('second');
      let offsetHeight = div.offsetHeight + 100;

      document.getElementById("height-not-fixed").style.height = offsetHeight + "px";
    };
  });