
window.addEventListener("load",function(){
    setTimeout(() =>{
        document.querySelector(".preloader").style.display="none";
    },3000)
});

const toogle = document.getElementById('toogle');
const navigation = document.getElementById('mob-nav');

toogle.onclick = function(){
    toogle.classList.toggle('active');
    navigation.classList.toggle('active');
}

document.onclick = function(e){
    if(e.target.id !== 'toogle' && e.target.id !== 'mob-nav'){
        toogle.classList.remove('active');
        navigation.classList.remove('active');
    }
}

const slider = document.getElementById('slider');
const slider1 = document.getElementById('slider1');
const slider2 = document.getElementById('slider2');
const slider3 = document.getElementById('slider3');
const slider4 = document.getElementById('slider4');
const slider5 = document.getElementById('slider5');
const slider6 = document.getElementById('slider6');
const slider7 = document.getElementById('slider7');
const slider8 = document.getElementById('slider8');

const project = document.getElementById('project');
const project1 = document.getElementById('project1');
const project2 = document.getElementById('project2');
const project3 = document.getElementById('project3');
const project4 = document.getElementById('project4');
const project5 = document.getElementById('project5');
const project6 = document.getElementById('project6');
const project7 = document.getElementById('project7');
const project8 = document.getElementById('project8');


slider.onclick = function(){
    project.classList.toggle('active');
}

slider1.onclick = function(){
    project1.classList.toggle('active');
}

slider2.onclick = function(){
    project2.classList.toggle('active');
}

slider3.onclick = function(){
    project3.classList.toggle('active');
}

slider4.onclick = function(){
    project4.classList.toggle('active');
}

slider5.onclick = function(){
    project5.classList.toggle('active');
}

slider6.onclick = function(){
    project6.classList.toggle('active');
}

slider7.onclick = function(){
    project7.classList.toggle('active');
}

slider8.onclick = function(){
    project8.classList.toggle('active');
}