import { Ball } from './ball.js';

var gForceVector;
var lastFrameDateTime;
var ball;

window.setup = function () {

    gForceVector = createVector(0, 5);
    lastFrameDateTime = millis();

    noStroke();
    smooth();

    ball = new Ball(10, 20, 20);

}

window.draw = function () {
    createCanvas(600, 600);
    background(220);

    const deltaTime = (millis() - lastFrameDateTime) / 1000;
    lastFrameDateTime = millis();

    ball.draw();

}
