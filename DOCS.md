##Classes: `World`, `Organism`

###Class: `World`
Usage: `World([args])`
Arguments: `world`, `width`, `height`, `color`

##Class: `World` -> Functions: `create`, `specs`

###Function: `create`
Usage: `[world].create()`
Arguments: None

###Function: `specs`
Usage: `[world].specs()`
Arguments: None

Example:
```python
earth = World(world='earth', width=500, height=500, color='#000')
earth.create()
earth_info = earth.specs()
print(earth_info)
```

###Class: `Organism`
Usage: `Organism([args])`
Arguments: `organism`, `size`, `color`, `xy`

##Class: `Organism` -> Functions: `create`, `specs`, `setspeed`, `setcoords`

###Function: `create`
Usage: `[organism].create()`
Arguments: None

###Function: `specs`
Usage: `[organism].specs()`
Arguments: None

###Function: `setspeed`
Usage: `[organism].setspeed([args])`
Arguments: `speed`

###Function: `setcoords`
Usage: `[organism].setcoords([args])`
Arguments: `xy`

Example:
```python
tim = Organism(organism='tim', size=10, color='#fff', xy=[0, 0])
tim.create()
tim_info = tim.specs()
print(tim_info)
tim.setcoords(xy=[0, 50])
print(tim_info)
tim.setspeed(speed=0)
```
