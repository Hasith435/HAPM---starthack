const a1 = document.getElementById('a1')
const a2 = document.getElementById('a2')
const a3 = document.getElementById('a3')
const a4 = document.getElementById('a4')


a1.addEventListener('click',select1)
a2.addEventListener('click',select2)
a3.addEventListener('click',select3)
a4.addEventListener('click',select4)

var selected = 'f'

function select1(){
    if (selected == 'f'){
        a1.style.backgroundColor = '#7AA39B'
        selected = 't'
    }else{
        a1.style.backgroundColor = '#7AA39B'
        a2.style.backgroundColor = '#B3C9C6'
        a3.style.backgroundColor = '#B3C9C6'
        a4.style.backgroundColor = '#B3C9C6'
        

    }
    
}
function select2(){
    
   
    if (selected == 'f'){
        selected = 't'
        a2.style.backgroundColor  = '#7AA39B'
    }else{
        a2.style.backgroundColor = '#7AA39B'
        a1.style.backgroundColor = '#B3C9C6'
        a3.style.backgroundColor = '#B3C9C6'
        a4.style.backgroundColor = '#B3C9C6'
        

    }
}
function select3(){
    

    if (selected == 'f'){
        selected = 't'
        a3.style.backgroundColor = '#7AA39B'
    }else{
        a3.style.backgroundColor = '#7AA39B'
        a1.style.backgroundColor = '#B3C9C6'
        a2.style.backgroundColor = '#B3C9C6'
        a4.style.backgroundColor = '#B3C9C6'
        

    }
}
function select4(){
  
    if (selected == 'f'){
        selected = 't'
        a4.style.backgroundColor = '#7AA39B'
    }else{
        a4.style.backgroundColor = '#7AA39B'
        a1.style.backgroundColor = '#B3C9C6'
        a2.style.backgroundColor = '#B3C9C6'
        a3.style.backgroundColor = '#B3C9C6'
        

    }
}
