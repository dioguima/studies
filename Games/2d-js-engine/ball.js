export class Ball {

    constructor(size, x, y) {
        this.size = size;
        this.x = x;
        this.y = y;
    }

    draw() {
        fill(220, 10, 10);
        ellipse(this.x, this.y, this.size, this.size);
    }

}