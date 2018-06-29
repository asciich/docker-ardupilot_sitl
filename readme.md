# Ardupilot SITL

This ```asciich/ardupilot_sitl``` container contains the complete "Software in the loop" Ardupilot autopilot simulator.
[The container is directly avialable from Docker Hub](https://hub.docker.com/r/asciich/ardupilot_sitl/)

If the docker option ```--net=host``` is used the default mavproxy ports (14550, 14550) are directly available.

## Simulate arducopter

To simmulate a arducopter vehicle use

```bash
docker run --net=host --rm -it asciich/ardupilot_sitl sim_arducopter
```

## Simulate arduplane

To simulate a arduplane vehicle use:

```bash
docker run --net=host --rm -it asciich/ardupilot_sitl sim_arduplane
```

## Test container

To test the ```asciich/ardupilot_sitl``` container use tox:

```bash
tox
```

## Additional information/ sources

* [Ardupilot SITL](http://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html)