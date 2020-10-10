import { Ball } from './ball.js';
import {Physics} from './physics.js'

var gForceVector;
var lastFrameDateTime;
var ball;
var physics = new Physics();

window.setup = function () {

    gForceVector = createVector(0, 5);
    lastFrameDateTime = millis();

    noStroke();
    smooth();

    ball = new Ball(30, 250, 20);

}

window.draw = function () {
    createCanvas(600, 600);
    background(220);

    const currentMillis = millis()
    const deltaTime = (currentMillis - lastFrameDateTime);
    lastFrameDateTime = currentMillis;

    physics.updateObject(ball, deltaTime);

    ball.draw();
}
