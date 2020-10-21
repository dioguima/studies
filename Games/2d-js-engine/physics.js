export class Physics{

    updateObject(object, deltaTime){

        const gravityVector = this.#createGravityVector(deltaTime);

        // console.log(object.velocity.y);

        object.velocity.y += gravityVector.y;

        if(object.checkCollision(object.x, 600)){
            object.y = 600 - object.size;
            object.velocity.y = object.velocity.y * -object.coefficientOfRestitution;
        }

        object.y += object.velocity.y;
    }

    #createGravityVector(deltaTime){
        return createVector(0, (10 * deltaTime)/1000);
    }

}