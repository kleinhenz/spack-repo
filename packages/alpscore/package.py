from spack import *


class Alpscore(CMakePackage):
    homepage = "https://github.com/ALPSCore/ALPSCore"
    url      = "https://github.com/ALPSCore/ALPSCore/archive/v2.2.0.tar.gz"
    git      = "https://github.com/ALPSCore/ALPSCore.git"

    version('master',       branch='master')
    version('2.2.0',        sha256='f7bc9c8f806fb0ad4d38cb6604a10d56ab159ca63aed6530c1f84ecaf40adc61')

    depends_on('boost')
    depends_on('eigen ~fftw ~metis ~mpfr ~scotch ~suitesparse')
    variant('accumulators', default=False, description="Enable legacy accumulators")
    variant('mc', default=False, description="Enable monte carlo")

    def cmake_args(self):
        alps_modules_disable=["accumulators", "mc"]
        if "+accumulators" in self.spec:
            alps_modules_disable.remove("accumulators")
        if "+mc" in self.spec:
            alps_modules_disable.remove("mc")

        args = ["-DALPS_CXX_STD=custom"]
        if len(alps_modules_disable):
            args.append("-DALPS_MODULES_DISABLE={:s}".format(";".join(alps_modules_disable)))

        return args
