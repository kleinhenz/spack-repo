from spack import *


class Hpx(CMakePackage):
    """C++ runtime system for parallel and distributed applications."""

    homepage = "http://stellar.cct.lsu.edu/tag/hpx/"
    url      = "https://github.com/STEllAR-GROUP/hpx/archive/1.3.0.tar.gz"

    version('1.3.0',     sha256='cd34da674064c4cc4a331402edbd65c5a1f8058fb46003314ca18fa08423c5ad')
    version('1.2.0',     sha256='20942314bd90064d9775f63b0e58a8ea146af5260a4c84d0854f9f968077c170')

    depends_on('boost')
    depends_on('jemalloc')
    depends_on('hwloc')
    depends_on('mpi')

    def cmake_args(self):
        args = ['-DHPX_BUILD_EXAMPLES=OFF', '-DHPX_WITH_MALLOC=jemalloc', '-DHPX_WITH_MAX_CPU_COUNT=128', '-DHPX_WITH_EXAMPLES=OFF']
        return args
