const backbtn = document.getElementById('back')
const dd = document.getElementById('dd')
const nav = document.getElementById('nav')
const home = document.getElementById('home')
const logout = document.getElementById('logout')
const words = document.querySelectorAll('.selection ul li a')
const contianer = document.getElementById('container')

const src2 = 'arrow_forward_ios_20dp_FILL0_wght400_GRAD0_opsz20.png'
const src1 = 'arrow_back_ios_20dp_FILL0_wght400_GRAD0_opsz20.png'

backbtn.addEventListener('click',()=>{
    nav.classList.toggle('nav-s')
    home.classList.toggle('hidden')
    logout.classList.toggle('hidden')
    contianer.classList.toggle('x-contianer')
    console.log(dd.src)
    if (dd.src.includes(src1)) {
        dd.src = src2;
    } else {
        dd.src = src1;
    }
    

    words.forEach((word)=>{
        word.classList.toggle('hidden')
    })
})
