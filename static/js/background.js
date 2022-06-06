let skyColor = '#110E19'; //ciel
    terrainColor = "#191D4C",
    starsColor = '#05004c',
    montain1Color = '#191d4c',
    montain2Color = "rgb(17,20,40)",
    montain3Color = "rgb(10,10,5)",
    fontColor = '#ffffff',
    night=true;

if (localStorage.getItem('theme')) {
  night=(localStorage.getItem('theme') == 'dark' ? false : true);
} else {
  if (prefersDarkTheme.matches) {
      night=true;
  } else {
    night=false;
  }
}

if (night) {
    skyColor = '#bddfde'; //ciel
    terrainColor = "#bbbbbb";
    starsColor = '#bddfde';
    montain1Color = '#b4d4d3';
    montain2Color = "#4e8a94";
    montain3Color = "#43787e"; // montagne 1er plan
    fontColor = '#bddfde'; // stars
    night=false;
} else {
    skyColor = '#110E19'; //ciel
    terrainColor = "#191D4C";
    starsColor = '#05004c';
    montain1Color = "#191d4c";
    montain2Color = "rgb(17,20,40)";
    montain3Color = "rgb(10,10,5)";
    fontColor = '#ffffff';
    night=true;
}

$('.theme-toggler').click(() => {
    if (night) {
        skyColor = '#bddfde'; //ciel
        terrainColor = "#bbbbbb";
        starsColor = '#bddfde';
        montain1Color = '#b4d4d3';
        montain2Color = "#4e8a94";
        montain3Color = "#43787e"; // montagne 1er plan
        fontColor = '#bddfde'; // stars
        night=false;
    } else {
        skyColor = '#110E19'; //ciel
        terrainColor = "#191D4C";
        starsColor = '#05004c';
        montain1Color = "#191d4c";
        montain2Color = "rgb(17,20,40)";
        montain3Color = "rgb(10,10,5)";
        fontColor = '#ffffff';
        night=true;
    }
});


(function () {
    var requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame || function (callback) {
            window.setTimeout(callback, 1000 / 60);
        };
    window.requestAnimationFrame = requestAnimationFrame;
})();

// Terrain stuff.
let background = document.getElementById("bgCanvas"),
    bgCtx = background.getContext("2d"),
    width = window.innerWidth,
    height = document.documentElement.clientHeight;

(height < 400) ? height = 400 : height;

background.width = width;
background.height = height;

function Terrain(options) {
    options = options || {};
    this.terrain = document.createElement("canvas");
    this.terCtx = this.terrain.getContext("2d");
    this.scrollDelay = options.scrollDelay || 90;
    this.lastScroll = new Date().getTime();

    this.terrain.width = width;
    this.terrain.height = height;
    this.fillStyle = options.fillStyle || montain1Color;
    this.mHeight = options.mHeight || height;

    // generate
    this.points = [];

    var displacement = options.displacement || 140,
        power = Math.pow(2, Math.ceil(Math.log(width) / (Math.log(2))));

    // set the start height and end height for the terrain
    this.points[0] = this.mHeight;//(this.mHeight - (Math.random() * this.mHeight / 2)) - displacement;
    this.points[power] = this.points[0];

    // create the rest of the points
    for (var i = 1; i < power; i *= 2) {
        for (var j = (power / i) / 2; j < power; j += power / i) {
            this.points[j] = ((this.points[j - (power / i) / 2] + this.points[j + (power / i) / 2]) / 2) + Math.floor(Math.random() * -displacement + displacement);
        }
        displacement *= 0.6;
    }

    document.body.appendChild(this.terrain);
}

Terrain.prototype.update = function () {
    // draw the terrain
    this.terCtx.clearRect(0, 0, width, height);
    this.terCtx.fillStyle = this.fillStyle;
    
    if (new Date().getTime() > this.lastScroll + this.scrollDelay) {
        this.lastScroll = new Date().getTime();
        this.points.push(this.points.shift());
    }

    this.terCtx.beginPath();
    for (var i = 0; i <= width; i++) {
        if (i === 0) {
            this.terCtx.moveTo(0, this.points[0]);
        } else if (this.points[i] !== undefined) {
            this.terCtx.lineTo(i, this.points[i]);
        }
    }

    this.terCtx.lineTo(width, this.terrain.height);
    this.terCtx.lineTo(0, this.terrain.height);
    this.terCtx.lineTo(0, this.points[0]);
    this.terCtx.fill();
}




// stars
function Star(options) {
    this.size = Math.random() * 2;
    this.speed = Math.random() * .05;
    this.x = options.x;
    this.y = options.y;
}

Star.prototype.reset = function () {
    this.size = Math.random() * 2;
    this.speed = Math.random() * .05;
    this.x = width;
    this.y = Math.random() * height;
}

Star.prototype.update = function () {
    this.x -= this.speed;
    if (this.x < 0) {
        this.reset();
    } else {
        bgCtx.fillRect(this.x, this.y, this.size, this.size);
    }
}

function ShootingStar() {
    this.reset();
}

ShootingStar.prototype.reset = function () {
    this.x = Math.random() * width;
    this.y = 0;
    this.len = (Math.random() * 80) + 10;
    this.speed = (Math.random() * 10) + 6;
    this.size = (Math.random() * 1) + 0.1;
    // this is used so the shooting stars arent constant
    this.waitTime = new Date().getTime() + (Math.random() * 3000) + 500;
    this.active = false;
}

ShootingStar.prototype.update = function () {
    if (this.active) {
        this.x -= this.speed;
        this.y += this.speed;
        if (this.x < 0 || this.y >= height) {
            this.reset();
        } else {
            bgCtx.lineWidth = this.size;
            bgCtx.beginPath();
            bgCtx.moveTo(this.x, this.y);
            bgCtx.lineTo(this.x + this.len, this.y - this.len);
            bgCtx.stroke();
        }
    } else {
        if (this.waitTime < new Date().getTime()) {
            this.active = true;
        }
    }
}

var entities = [];

// init the stars
for (var i = 0; i < height; i++) {
    entities.push(new Star({
        x: Math.random() * width,
        y: Math.random() * height
    }));
}

// Add 2 shooting stars that just cycle.

stars1 = new ShootingStar();
stars2 = new ShootingStar();
montain1 = new Terrain({mHeight : (height/2)-120, fillStyle : montain1Color});
montain2 = new Terrain({displacement : 120, scrollDelay : 50, fillStyle : montain2Color, mHeight : (height/2)-60});
montain3 = new Terrain({displacement : 100, scrollDelay : 20, fillStyle : montain3Color, mHeight : height/2});

entities.push(stars1);
entities.push(stars2);
entities.push(montain1);
entities.push(montain2);
entities.push(montain3);

//animate background
function animate() {
    // Second canvas used for the stars
    stars1.fillStyle = starsColor;
    stars2.fillStyle = starsColor;
    montain1.fillStyle = montain1Color;
    montain2.fillStyle = montain2Color;
    montain3.fillStyle = montain3Color;

    bgCtx.fillStyle = skyColor;
    bgCtx.fillRect(0, 0, width, height);
    
    bgCtx.fillRect(0, 0, width, height);
    bgCtx.fillStyle = fontColor;
    bgCtx.strokeStyle = fontColor;

    var entLen = entities.length;

    while (entLen--) {
        entities[entLen].update();
    }
    requestAnimationFrame(animate);
}
animate();
