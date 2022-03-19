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
