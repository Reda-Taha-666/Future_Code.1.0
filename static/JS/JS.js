$(document).ready(function () {
  // إضافة تأثيرات للتنقل السلس
  $("a.nav-link").on("click", function (event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $("html, body").animate(
        {
          scrollTop: $(hash).offset().top - 80,
        },
        800
      );
    }
  });

  // تأثير للكروت عند التمرير
  $(window).scroll(function () {
    $(".card").each(function () {
      var position = $(this).offset().top;
      var scroll = $(window).scrollTop();
      var windowHeight = $(window).height();

      if (scroll > position - windowHeight + 200) {
        $(this).addClass("fade-in");
      }
    });
  });

 
});
