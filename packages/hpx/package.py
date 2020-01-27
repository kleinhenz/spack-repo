from spack import *


class Hpx(CMakePackage):
    """C++ runtime system for parallel and distributed applications."""

    homepage = "http://stellar.cct.lsu.edu/tag/hpx/"
    url      = "https://github.com/STEllAR-GROUP/hpx/archive/1.3.0.tar.gz"
    git      = "git@github.com:STEllAR-GROUP/hpx.git"

    version('1.4.0', tag='1.4.0')
    version('1.3.0', tag='1.3.0')
    version('1.2.0', tag='1.2.0')

    depends_on('boost cxxstd=14')
    depends_on('jemalloc')
    depends_on('hwloc')
    depends_on('mpi')

    def cmake_args(self):
        args = ['-DHPX_BUILD_EXAMPLES=OFF', '-DHPX_WITH_MALLOC=jemalloc', '-DHPX_WITH_MAX_CPU_COUNT=128', '-DHPX_WITH_EXAMPLES=OFF', '-DHPX_WITH_CXX14=ON']
        return args

    def check(self):
        """Searches the CMake-generated Makefile for the target ``test`` and runs it if found.
        """
        with working_dir(self.build_directory):
            if self.generator == 'Unix Makefiles':
                self._if_make_target_execute('tests')
                self._if_make_target_execute('test')
            elif self.generator == 'Ninja':
                self._if_ninja_target_execute('tests')
                self._if_ninja_target_execute('test')
