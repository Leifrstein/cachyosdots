// ==UserScript==
// @name        startpage.com ad-block
// @namespace   startpage.com
// @description remove <div id="adBlock"> from startpage.com results
// @include     https://startpage.com/*
// @include     https://*.startpage.com/*
// @version  1
// @run-at      document-start
// ==/UserScript==
window.addEventListener('load', function() {
  document.getElementById("adBlock").style.display = "none";
  //console.log("searchpage adblock fired...")
}, false);

