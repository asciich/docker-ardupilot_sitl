import pytest

@pytest.fixture(scope='module')
def container_image():
    return 'asciich/ardupilot_sitl'

def startup_scripts():
    return [
        'sim_arducopter',
        'sim_arduplane',
    ]

class TestAsciichArdupilotSitlImage(object):

    def test_sim_vehicle_py_in_path(self, docker_container):
        assert docker_container.exists('sim_vehicle.py')

    @pytest.mark.parametrize('startup_script', startup_scripts())
    def test_sim_startup_scripts_exists(self, docker_container, startup_script):
        assert docker_container.exists(startup_script)

    @pytest.mark.parametrize('startup_script', startup_scripts())
    def test_simulation_can_be_started(self, docker_container, startup_script):
        timeout_return_value = 124
        assert docker_container.run_expect('timeout 10 {}'.format(startup_script), timeout_return_value)