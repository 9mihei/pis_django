$(document).ready(function() {
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.logo');
    
    $(window).scroll(function() {
        var scrolled = $(window).scrollTop();
        
        // Движение иконок
        $parallaxElements.each(function(index) {
            var speed = 0.15 * (index + 1);
            var yPosition = scrolled * speed;
            $(this).css({
                'transform': 'translateY(' + yPosition + 'px)'
            });
        });
        
        // Движение логотипа (увеличил скорость)
        if ($logo.length) {
            var logoPosition = scrolled * 1;  
            $logo.css({
                'transform': 'translateY(' + logoPosition + 'px)'
            });
        }
    });
});