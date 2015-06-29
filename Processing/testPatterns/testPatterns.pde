PVector mLoc, mDir;
int SPEED = 4;
int DIAMETER = 200;

void setup() {
  size(600, 600);
  stroke(0);
  fill(0);
  mLoc = new PVector(-DIAMETER, -DIAMETER);
  mDir = new PVector(-1, -1);
}

void draw() {
  background(255);
  mLoc.add(PVector.mult(mDir,SPEED));

  if (mLoc.x > width+DIAMETER || mLoc.x<-DIAMETER || mLoc.y>height+DIAMETER || mLoc.y<-DIAMETER) {
    mLoc.set(int(random(0, 3))*width/2, int(random(0, 3))*height/2);
    if (mLoc.x == width/2 && mLoc.y == height/2) mLoc.x = 0;
    mDir.set((mLoc.x>0)?-1:1, (mLoc.y>0)?-1:1);
    if (mLoc.x == width/2) mDir.x = 0;
    else if (mLoc.y == height/2) mDir.y = 0;
  }
  ellipse(mLoc.x, mLoc.y, DIAMETER, DIAMETER);
}

