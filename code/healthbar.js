window.HealthBar = function(x, y, width, height) {
  this.x = x;
  this.y = y;
  this.width = width;
  this.height = height;
  this.border = Crafty.e('2D', 'Canvas', 'Color')
    .attr({x: x, y: y, w: width, h: height})
    .color('grey');
  this.health = Crafty.e('2D', 'Canvas', 'Color')
    .attr({x: x+1, y: y+1, w: width-2, h: height-2})
    .color('green');
  
  // The width goes from 0 to width-2. Percentages should map onto that range.
  this.setPercent = function(percent) {
    if (percent < 0) {
      percent = 0;
    }
    this.health.w = (this.width-2) * (percent/100);
  };
  this.getPercent = function() {
    var percent = (this.health.w / (this.width-2)) * 100;
    if (percent > 100) {
      percent = 100;
    }
    return percent;
  };
};
