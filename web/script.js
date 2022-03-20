var img;
// var pg;
function preload() {
  img = loadImage("../assets/spiral.jpg");
}

function setup() {
  createCanvas(400, 800);
  // pg = createGraphics(400, 400);
}

function mousePressed() {
  // pg.fill(0, 0, 0);
  // pg.ellipse(mouseX, mouseY, 5, 5);
  rect(mouseX, mouseY, 5, 5);
  strokeWeight(10);
}

var scribble = new Scribble();
function draw() {
  // image(img, 0, 0, 400, 400);
  // image(pg, 0, 0);
  // image(pg, 0, 400);
  if (mouseIsPressed) {
    scribble.scribbleLine(mouseX, mouseY, mouseX, mouseY);
    strokeWeight(10);
  }
}

// function draw() {
//   if (mouseIsPressed) {
//     fill(255);
//     noStroke();
//     rect(mouseX, mouseY, 5, 5);
//     strokeWeight(10);
//   }
// }
// function clear() {
//   erase();
//   background(100);
//   }

var symp = document.getElementById("symptoms");
var symptoms = parseInt(symp.value);

var st = document.getElementById("stand");
var stand = parseInt(st.value);

var wh = document.getElementById("wheelchair");
var wheelchair = parseInt(wh.value);

var total = symptoms + stand + wheelchair;
var show;
var desc;
if (total >= 6) {
  show = "SEVERE";
  desc = ":0";
} else if (total < 6 && total > 4) {
  show = "MODERATE";
  desc =
    "You've been down the road but haven't rolled yet so continue to practice the resources attached below.";
} else {
  show = "MILD";
  desc =
    "Say it with me! Yaayyy! I'm all pumped up. That's pretty good, and I think I have energy for at least 4 more hills. I'm going to run and run and run! I can do this. I'm too youthful!!! I will keep up with my healthy mindset and happy soul. It's so nice to see the scale moving in the right direction. I am stable in all ways! LOOK! I can stand and walk gracefully and intently! I am able to control my momentum! To continue to prevent the futhering of Parkinson's, see the resources attached below.";
}
function onSubmit() {
  // p.innerHTML += "We have detected that you have mild symtoms."
  // document.getElementById(“result”).innerText +=  “data”;

  alert(`${total} We have detected that you have ${show} symtoms. ${desc}`);
}
