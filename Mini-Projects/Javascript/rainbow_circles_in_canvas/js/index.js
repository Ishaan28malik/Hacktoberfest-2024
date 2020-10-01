"use strict";
const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const mouse = {
	x: window.innerWidth / 2,
	y: window.innerHeight / 2,
	isDown: false
};

window.addEventListener("mousedown", function() {
	mouse.isDown = true;
});

window.addEventListener("mouseup", function() {
	mouse.isDown = false;
});

window.addEventListener("mousemove", function(event) {
	mouse.x = event.clientX;
	mouse.y = event.clientY;
});

window.addEventListener("resize", function() {
	canvas.width = window.innerWidth;	
	canvas.height = window.innerHeight;
});

window.addEventListener("click", function() {

});

canvas.addEventListener("touchstart", function() {
	mouse.isDown = true;
});

canvas.addEventListener("touchmove", function(event) {
  event.preventDefault();
  mouse.x = event.touches[0].pageX;
  mouse.y = event.touches[0].pageY;
});

canvas.addEventListener("touchend", function() {
  mouse.isDown = false;
});

function Circle(x, y, radius, color, xVelocity, yVelocity) {
	this.x = x;
	this.y = y;
	this.radius = radius;
	this.color = color;
	this.velocity = {
		x: xVelocity,
		y: yVelocity
	};
	this.isAlive = true;

	this.update = function() {
		if (this.x - this.radius > canvas.width || this.x + this.radius < 0 || this.y - this.radius > canvas.height || this.y + this.radius < 0) {
			this.isAlive = false;
		}

		this.x += this.velocity.x;
		this.y += this.velocity.y;
		this.draw();
	};

	this.draw = function() {
		c.beginPath();
		c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);	
		c.fillStyle = this.color;
		c.fill();
		c.closePath();
	};
}

function Explosion(velocity, hue) {
	this.particles = [];
	this.particleAmount = 50;
	this.particleSeparation = (Math.PI * 2) / this.particleAmount;

	this.init = function() {
		let distance = this.particleSeparation;

		for (let i = 0; i < this.particleAmount; i++) {
			let radius = 4;
			let color = 'hsl(' + hue + ', 100%, 50%)';
			
			this.particles.push(new Circle(mouse.x, mouse.y, radius, color, Math.sin(distance) * velocity, Math.cos(distance) * velocity));

			distance += this.particleSeparation;
		}
	};

	this.init();

	this.update = function() {
		for (let i = 0; i < this.particles.length; i++) {
			if (this.particles[i].isAlive === false)
				this.particles.splice(i, 1);	
		
			// Placed below splice since having it above caused particles to flash
			if (this.particles[i] !== undefined)	
				this.particles[i].update();
		}
	};
}

let timer = 0;
let explosions = [];
let hue = 214;
let isHueIncreasing = false;

function animate() {
	window.requestAnimationFrame(animate);
	timer += 1;
	c.fillStyle = '#111';
	c.fillRect(0, 0, canvas.width, canvas.height);
	
	if (timer % 12 === 0) {	
		if (hue > 0 && isHueIncreasing === false) {
			hue -= 2;
		} else {
			hue += 2;
		}

		if (hue <= 0) {
			isHueIncreasing = true;
		} else if(hue >= 254) {
			isHueIncreasing = false;
		}
		explosions.push(new Explosion(2, hue));

	}

	for (let i = 0; i < explosions.length; i++) {
		explosions[i].update();
	}

}

animate();