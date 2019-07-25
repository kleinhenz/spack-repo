from spack import *


class Alpscore(CMakePackage):
    homepage = "https://github.com/ALPSCore/ALPSCore"
    url      = "https://github.com/ALPSCore/ALPSCore/archive/v2.2.0.tar.gz"
    git      = "https://github.com/ALPSCore/ALPSCore.git"

    version('master',       branch='master')
    version('2.2.0',        sha256='f7bc9c8f806fb0ad4d38cb6604a10d56ab159ca63aed6530c1f84ecaf40adc61')

    depends_on('boost')
    depends_on('eigen ~fftw ~metis ~mpfr ~scotch ~suitesparse')

    def cmake_args(self):
        args = []
        return args
