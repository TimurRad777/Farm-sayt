let first_tree = document.querySelector('.first_tree')
let second_tree = document.querySelector('.second_tree')

first_tree.onclick = function(){
    first_tree.classList.toggle('open')
    second_tree.classList.remove('open')
}
second_tree.onclick = function(){
    second_tree.classList.toggle('open')
    first_tree.classList.remove('open')
}