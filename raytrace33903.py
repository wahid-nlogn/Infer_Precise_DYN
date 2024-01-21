

import array
import math
import time
from six.moves import xrange


DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 100
EPSILON = 0.00001
ZERO = (0, 0, 0)#vector(0, 0, 0)
RIGHT = (1, 0, 0)#vector(1, 0, 0)
UP = (0, 1, 0)#vector(0, 1, 0)
OUT = (0, 0, 1)#vector(0, 0, 1)

def vector(initx, inity, initz)->Tuple(Dyn,Dyn,Dyn):
    return (initx, inity, initz)

def dot(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))->float:
    #other.mustBeVector()
    (x,y,z) = vec
    (x1, y1, z1) = other
    return (x * x1 * 1.0) + (y * y1 * 1.0) + (z * z1 * 1.0)

def magnitude(vec:Tuple(Dyn,Dyn,Dyn))->float:
    return (math.sqrt(dot(vec, vec)) + 0.0)

def add(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))-> Tuple(Dyn,Dyn,Dyn):
    (x,y,z) = vec
    (x1,y1,z1) = other
    return (x+x1, y+y1, z+z1)
    #if other.isPoint():
        #return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    #else:
        #return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

def sub(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):
    #other.mustBeVector()
    (x,y,z) = vec
    (x1,y1,z1) = other
    return vector(x - x1, y - y1, z - z1)

def scale(vec:Tuple(Dyn,Dyn,Dyn), factor)->Tuple(Dyn,Dyn,Dyn):
    x,y,z = vec
    return (factor * x, factor * y, factor * z)

def cross(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):
    #other.mustBeVector()
    (x,y,z) = vec
    (x1,y1,z1) = other
    return (y * z1 - z * y1,
                      z * x1 - x * z1,
                      x * y1 - y * x1)

def normalized(vec:Tuple(Dyn,Dyn,Dyn))-> Tuple(Dyn,Dyn,Dyn):
    return scale(vec, 1.0 / magnitude(vec))

def negated(vec:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):
    return scale(vec, -1)

def eq(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))->Bool:
    x,y,z = vec
    x1,y1,z1 = other
    return (x == x1) and (y == y1) and (z == z1)

def reflectThrough(vec:Tuple(Dyn,Dyn,Dyn), normal:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):
    d = scale(normal, dot(vec, normal))
    return sub(vec, scale(d,2))

def sphere(centre, radius)->Tuple(Dyn,Dyn):
    #centre.mustBePoint()
    #self.centre = centre
    #self.radius = radius
    return (centre, radius)
def ray(point, vect:Tuple(Dyn,Dyn,Dyn)):
    #self.point = point
    #self.vector = vector.normalized()
    return (point, normalized(vect))

def pointAtTime(ray, t)->Tuple(Dyn,Dyn,Dyn):
    point, vector = ray
    return add(point, scale(vector, t))

def intersectionTime(s:Tuple(Tuple(Dyn,Dyn,Dyn),Dyn), ra:Tuple(Tuple(Dyn,Dyn,Dyn),Tuple(Dyn,Dyn,Dyn))):
    (centre, radius) = s
    (point, vect) = ra
    cp = sub(centre, point)
    v = dot(cp, vect)
    discriminant = (radius * radius) - (dot(cp, cp) - v * v)
    if discriminant < 0:
        return None
    else:
        return v - math.sqrt(discriminant)

def normalAt(s:Tuple(Tuple(Dyn,Dyn,Dyn),Dyn), p:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):
    (centre, radius) = s
    return normalized((sub(p,  centre)))
    
def halfspace(point, normal:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn, Tuple(Dyn,Dyn,Dyn)):
    #self.point = point
    #self.normal = normal.normalized()
    return (point, normalized(normal))
def canvas(width, height)->Tuple(Dyn,Dyn,int):
    byts = array.array('B', [0] * (width * height * 3))
    #byts = [0] * (width * height * 3)
    for i in xrange(width * height):
        #0
        byts[i * 3 + 2] = 255
    #self.width = width
    #self.height = height
    return (byts, width, height)

def plot(canv:Tuple(Dyn,Dyn,Dyn), x:int, y:int, r:int, g:int, b:int):
    (byts, width, height) = canv
    i = ((height - y - 1) * width + x) * 3
    byts[i] = max(0, min(255, int(r * 255)))
    byts[i + 1] = max(0, min(255, int(g * 255)))
    byts[i + 2] = max(0, min(255, int(b * 255)))
    return None

def firstIntersection(intersections:List(Dyn)):
    result = None
    for i in intersections:
        candidateT = i[1]
        if candidateT is not None and candidateT > -EPSILON:
            if result is None or candidateT < result[1]:
                result = i
    return result

def scene()->Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Int):
    objects = []
    lightPoints = []
    position = vector(0.0, 1.8, 10.0)
    lookingAt = (0.0,0.0,0.0)#Point.ZERO
    fieldOfView = 45
    recursionDepth = 0
    return (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth)

def moveTo(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), p)->Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn):
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    position = p
    return (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth)

def lookAt(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), p)->Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn):
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    lookingAt = p
    return (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth)

def addObject(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), object, surface)-> Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn):
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    objs = [] + objects
    objs.append((object, surface))
    return (objs, lightPoints, position, lookingAt, fieldOfView, recursionDepth)

def addLight(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), p)->Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn):
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    lps = [] + lightPoints
    lps.append(p)
    return (objects, lps, position, lookingAt, fieldOfView, recursionDepth)

def addColours(a, scale, b)->Tuple(Dyn,Dyn,Dyn):
    return (a[0] + scale * b[0],
            a[1] + scale * b[1],
            a[2] + scale * b[2])

def baseColourAt(ss:Tuple(Dyn,Dyn,Dyn,Dyn), p):
    (baseColour, specularCoefficient, lambertCoefficient, ambientCoefficient) = ss
    return baseColour

def render(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), canvas1):
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    fovRadians = math.pi * (fieldOfView / 2.0) / 180.0
    halfWidth = math.tan(fovRadians)
    halfHeight = 0.75 * halfWidth
    width = halfWidth * 2
    height = halfHeight * 2
    bytes, w, h = canvas1
    pixelWidth = width / (w - 1)
    pixelHeight = height / (h - 1)

    eye = ray(position, sub(lookingAt, position))
    p, v = eye    
    vpRight = normalized(cross(v, UP))
    vpUp = normalized(cross(vpRight, v))

    for y in xrange(int(height)):
        for x in xrange(int(width)):
            xcomp = scale(vpRight, x * pixelWidth - halfWidth)
            ycomp = scale(vpUp, y * pixelHeight - halfHeight)
            r = ray(p, add(add(v, xcomp), ycomp))
            #colour = rayColour(sc, r)
            #plot(canvas1, x, y, *colour)

    return None

def lightIsVisible(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), l, p):
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    for (o, s) in objects:
        t = intersectionTime(o, ray(p, sub(l, p)))
        if t is not None and t > EPSILON:
            return False
    return True

def visibleLights(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), p):
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    result = []
    for l in lightPoints:
        if lightIsVisible(sc, l, p):
            result.append(l)
    return result

def simpleSurface(baseColour)->Tuple(Dyn,Float,Float,Dyn):
    #baseColour = kwargs.get('baseColour', (1, 1, 1))
    specularCoefficient = 0.2
    lambertCoefficient =  0.6
    ambientCoefficient = 1.0 - specularCoefficient - lambertCoefficient
    return (baseColour, specularCoefficient, lambertCoefficient, ambientCoefficient)

def bench_raytrace(loops, width, height, filename):
    range_it = xrange(loops)
    #t0 = perf.perf_counter()

    for i in range_it:
        #canvas1 = canvas(width, height)
        s = scene()
        addLight(s, vector(30, 30, 10))
        addLight(s, vector(-10, 100, 30))
        lookAt(s, vector(0, 3, 0))
        addObject(s, sphere(vector(1, 3, -10), 2),
                    simpleSurface((1, 1, 0)))
        for y in xrange(6):
            addObject(s,sphere(vector(-3 - y * 0.4, 2.3, -5), 0.4),
                        simpleSurface((y / 6.0, 1 - y / 6.0, 0.5)))
            scale(normalized(vector(10,23,19)), y * 11)
        #s.addObject(Halfspace(Point(0, 0, 0), Vector.UP),
        #            CheckerboardSurface())
        #render(s,canvas1)
    return None



    #dt = perf.perf_counter() - t0

    #if filename:
    #    canvas.write_ppm(filename)
    #return dt
def main():
    t0 = time.time()
    bench_raytrace(100, DEFAULT_WIDTH, DEFAULT_HEIGHT, "raytrace.ppm")
    t1 = time.time()
    print(t1-t0)

main()

