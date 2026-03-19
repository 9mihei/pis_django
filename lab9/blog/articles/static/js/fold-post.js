var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        var post = event.target.closest('.one-post');
        
        if (post.classList.contains('folded')) {
            post.classList.remove('folded');
            event.target.textContent = 'Свернуть';
        } else {
            post.classList.add('folded');
            event.target.textContent = 'Развернуть';
        }
    });
}