# Ardupilot SITL

This ```asciich/ardupilot_sitl``` container contains the complete "Software in the loop" Ardupilot autopilot simulator.

If the docker option ```--net=host``` is used the default mavproxy ports (14550, 14550) are direclty available.

## Simulate arducopter

To simmulate a arducopter vehicle use

```bash
docker run --net=host --rm -it asciich/adrupilot_sitl sim_arducopter
```

## Simulate arduplane

To simulate a arduplane vehicle use:

```bash
docker run --net=host --rm -it asciich/adrupilot_sitl sim_arduplane
```

## Test container

To test the ```asciich/ardupilot_sitl``` container use tox:

```bash
tox
```

## Additional information/ sources

* [Ardupilot SITL](http://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html)