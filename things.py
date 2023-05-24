import wikipedia
import random

a='''zipper
toe ring
socks
pool stick
video games
doll
beef
cat
water bottle
air freshener
hair tie
carpet
DVD
oil lamp
sand paper
chair
rubber duck
mp3 player
pencil
mirror
flag
couch
soap
twezzers
towel
face wash
nail file
white out
piano
Sewing needle
rubber band
ipod
shawl
eye liner
sofa
tooth picks
credit card
paint brush
pillow
sticky note
ear phones
bananas
air conditioner
scotch tape
chalk
sketch pad
leg warmers
sun glasses
clothes
perfume
flowers
bed
mouse pad
watch
chocolate
buckel
rusty nail
blouse
knife
sailboat
playing card
computer
paper
USB drive
brocolli
door
packing peanuts
key chain
candy wrapper
lace
stockings
bottle
newspaper
wallet
clay pot
puddle
apple
vase
deodorant
bowl
clock
toothbrush
magnet
car
cell phone
cinder block
bread
bag
synthesizer
milk
money
typewriter
street lights
glass
shirt
wagon
blanket
slipper
micro-USB
lamp shade
nail clippers
glow stick
shoe lace
spoon
tissue box
television
seat belt
tableware
soy sauce packet
toilet
carrots
fake flowers
book
button
window
pen
fridge
bracelet
photo album
lip gloss
clothes hanger
soda can
sharpie
plastic fork
thermometer
candle
checkbook
grid paper
cup
tree
eraser
bottle cap
mop
sidewalk
glasses
canvas
sandal
thermostat
pants
radio
ice cube tray
shampoo
floor
boom box
fork
drill press
helmet
bow and arrow
remote control
chapter book
balloon
shoes
sponge
screw
desk
ring
greeting card
washing machine
box
tire swing
Who Stole the Cookie from the Cookie Jar?
loudspeaker
toothpaste
lotion
shovel
food
phone
hair brush
picture frame
coasters
stop sign
monitor lizard
model car'''
l=list(a.split('\n'))
things={}
for a in l:
    p=str(wikipedia.summary(a,sentences=5))
    things[a]=[random.randint(100,1000000),'',p]
print(things)    
