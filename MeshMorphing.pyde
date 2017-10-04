from SVector import *
from BREP import BREP
from PIP import PIP

rotate_flag = True    # automatic rotation of model?
just_edges = False
time = 0.0   # keep track of passing time, for automatic rotation
A = None
B = None
p = None
r = False
interpolate = False

# initalize stuff
def setup():
    size (600, 600, OPENGL)
    noStroke()
    global A
    global B
    global p
    A = read_mesh ('octa.ply')
    B = read_mesh ('tetra.ply')
    p = PIP(A, B)


    
    
    # draw the current mesh
def draw():
    global A
    global B
    global p
    global time
    
    background(0)    # clear screen to black
    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    scale (1, -1, 1)    # change to right-handed coordinate system
    
    # create an ambient light source
    ambientLight (102, 102, 102)
  
    # create two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    pushMatrix();

    if just_edges:
        stroke(50, 50, 200)
        noFill()
    else:
        fill (50, 50, 200)            # set polygon color
        noStroke()
    ambient (200, 200, 200)
    specular (0, 0, 0)            # no specular highlights
    shininess (1.0)
    
    if rotate_flag:
        rotate (time, 1.0, 0.0, 0.0)
  
    if not p:
        beginShape()
        normal (0.0, 0.0, 1.0)
        vertex (-1.0, -1.0, 0.0)
        vertex ( 1.0, -1.0, 0.0)
        vertex ( 1.0,  1.0, 0.0)
        vertex (-1.0,  1.0, 0.0)
        endShape(CLOSE)
    else:
        p.drawSelf((sin(time)+1)/2)
            
    popMatrix()
    
    # maybe step forward in time (for object rotation)
    time += 0.01
        
        
# process key presses
def keyPressed():
    global A
    global B
    global p
    global r
    global just_edges
    global rotate_flag

    if key == '1':
        B = A
        A = read_mesh ('tetra.ply')
        p = PIP(A, B)
    elif key == '2':
        B = A
        A = read_mesh ('octa.ply')
        p = PIP(A, B)
    elif key == '3':
        B = A
        A = read_mesh ('icos.ply')
        p = PIP(A, B)
    elif key == '4':
        B = A
        A = read_mesh ('star.ply')
        p = PIP(A, B)
    elif key == 'e':
        just_edges = not just_edges
        pass  # toggle per-vertex shading
    elif key == 'r':
        rotate_flag = not rotate_flag
    elif key == 'q':
        exit()
        
def read_mesh(filename):
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    # print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    # print "number of faces =", num_faces
    
    verts = []
    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        verts.append(SVector(x, y, z))
        # print "vertex = ", verts[i]
    
    # read in the faces
    tris = []
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        
        tri = []
        for v in range(nverts):
            tri.append(int(words[v + 1]))

        # print "face =", tri[0], tri[1], tri[2]
        tris.append(tri)
        
    return BREP(tris, verts)