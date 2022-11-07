
 <script type="text/javascript">
      var days = 0;
      var hash = document.URL.substr(document.URL.indexOf('#')+1);
      var lang = (typeof(hash) === "string" && hash != "" && hash.length == 2) ? hash : "en";

      $( document ).ready(function() {
        var OneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
        var announced = new Date(2015,7,11); // 0 is January for some ungodly reason
        var today = new Date();
        announced = moment(announced);
        today = moment(today);
        days = today.diff(announced, 'days');
        updateText(lang);
      });

      
      @function
        updateText - called from the dropdown menu on top to change the language on the page
      @param
        language (string) - short code of the language to change
      function updateText(language) {
        'use strict';
        var i18n = $.i18n();;
        lang = language; // update the global variable as well
        i18n.locale = language;
        i18n.load( 'i18n/aadhaarsc-' + $.i18n().locale + '.json', language ).done( function(){
        $("*[data-i18n]").each(function(){
          $(this).text($.i18n($(this).data('i18n')))
        });
        $("[data-i18n='aadhaar-sc-days']").text($.i18n('aadhaar-sc-days', days));
        $("[data-i18n='aadhaar-sc-update-1']").text($.i18n('aadhaar-sc-update', 701));
        $("[data-i18n='aadhaar-sc-update-2']").text($.i18n('aadhaar-sc-update', 744));

        // update the share controls with the current language
        $("#shareButton").jsSocials("destroy");
        $("#shareButton").jsSocials({
          url: "http://aadhaarcases.in/#"+lang,
          text: $.i18n('aadhaar-sc-share-text', days),
          showLabel: false,
          showCount: false,
          shareIn: "popup",
          shares: ["email", "twitter", "facebook", "whatsapp", "linkedin", "telegram"]
        });
        });
      }

 </script>
