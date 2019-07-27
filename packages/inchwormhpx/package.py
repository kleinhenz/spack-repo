from spack import *


class Inchwormhpx(CMakePackage):
    homepage = "https://github.com/CQMP/InchwormHPX"
    git      = "git@github.com:CQMP/InchwormHPX.git"

    version('master',       branch='master')

    depends_on('hpx')
    depends_on('boost')
    depends_on('eigen ~fftw ~metis ~mpfr ~scotch ~suitesparse')
    depends_on('alpscore@master')

    def cmake_args(self):
        args = ["-DINCLEXCL_SUMMATION=OFF", "-DENABLE_DEBUG_PRINT=OFF", "-DENABLE_ASSERTS=ON", "-DENABLE_FILL_NAN=ON", "-DBenchmark=ON", "-DTesting=ON"]

        return args
