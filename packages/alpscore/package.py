from spack import *


class Alpscore(CMakePackage):
    homepage = "https://github.com/ALPSCore/ALPSCore"
    git      = "git@github.com:ALPSCore/ALPSCore.git"

    version('master',       branch='master')
    version('2.2.0',        tag='v2.2.0')

    depends_on('hdf5')
    depends_on('boost')
    depends_on('eigen ~fftw ~metis ~mpfr ~scotch ~suitesparse')
    variant('accumulators', default=False, description="Enable legacy accumulators")
    variant('mc', default=False, description="Enable monte carlo")

    variant('cxxstd',
            default='c++11',
            values=('c++03', 'c++11', 'c++14', 'custom'),
            multi=False,
            description='Use the specified C++ standard when building.')

    def cmake_args(self):
        alps_modules_disable=["accumulators", "mc"]
        if "+accumulators" in self.spec:
            alps_modules_disable.remove("accumulators")
        if "+mc" in self.spec:
            alps_modules_disable.remove("mc")

        args = ["-DALPS_CXX_STD=custom"]
        if len(alps_modules_disable):
            args.append("-DALPS_MODULES_DISABLE={:s}".format(";".join(alps_modules_disable)))

        cxxstd = self.spec.variants['cxxstd'].value
        args.append("-DALPS_CXX_STD={:s}".format(cxxstd))

        return args
