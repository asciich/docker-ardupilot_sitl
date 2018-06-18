import pytest

@pytest.fixture(scope='module')
def container_image():
    return 'asciich/ardupilot_sitl'

class TestAsciichAvrdudeImage(object):

    def test_sim_vehicle_py_in_path(self, docker_container):
        assert docker_container.exists('sim_vehicle.py')

    @pytest.mark.parametrize('startup_script', [
        'sim_arducopter',
        'sim_arduplane'
    ])
    def test_sim_startup_scripts_exists(self, docker_container, startup_script):
        assert docker_container.exists(startup_script)
