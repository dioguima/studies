export class Ball {

    constructor(size, x, y, mass, coefficientOfRestitution) {
        this.size = size;
        this.yVelocity = 0;
        this.velocity = createVector(0, 0);
        this.x = x;
        this.y = y;
        this.mass = mass;
        this.coefficientOfRestitution = coefficientOfRestitution || 0.5;
    }

    checkCollision(x, y){
        return this.y + this.size / 2 >= y;
    }

    draw() {
        fill(220, 10, 10);
        ellipse(this.x, this.y, this.size, this.size);
    }

}