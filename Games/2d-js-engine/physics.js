export class Physics{

    updateObject(object, deltaTime){

        const gravityVector = this.#createGravityVector(deltaTime);

        // console.log(object.yVelocity);

        // if(object.yVelocity < 0.01){
        //     object.yVelocity = 0;
        // }


        object.velocity.y += gravityVector.y;

        if(object.checkCollision(object.x, 600)){
            // debugger;
            // console.log(object);
            // console.log(this.yVelocity * this.coefficientOfRestitution);
            
            object.y = 600 - object.size;
            object.velocity.y = object.velocity.y * object.coefficientOfRestitution * -1;
        }

        object.y += object.velocity.y;
    }

    #createGravityVector(deltaTime){
        return createVector(0, (10 * deltaTime)/1000);
    }

}