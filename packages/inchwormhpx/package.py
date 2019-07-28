from spack import *

class Inchwormhpx(CMakePackage):
    homepage = 'https://github.com/CQMP/InchwormHPX'
    git      = 'git@github.com:CQMP/InchwormHPX.git'

    version('master',       branch='master')
    variant('python', default=False, description='install python tools')

    #TODO versions
    depends_on('hpx@1.3.0')
    depends_on('boost')
    depends_on('eigen')
    depends_on('alpscore@master')

    extends('python', when='+python')
    depends_on('python@3.6:',   type=('build', 'run'), when='+python')
    depends_on('py-pip',        type=('build', 'run'), when='+python')
    depends_on('py-numpy',      type='run', when='+python')
    depends_on('py-h5py',       type='run', when='+python')
    depends_on('py-matplotlib', type='run', when='+python')

    def cmake_args(self):
        spec = self.spec

        args = ['-DINCLEXCL_SUMMATION=OFF',
                '-DENABLE_DEBUG_PRINT=OFF',
                '-DENABLE_ASSERTS=ON',
                '-DENABLE_FILL_NAN=ON',
                '-DBenchmark=ON',
                '-DTesting=ON']

        if '+python' in spec:
          args.append('-DPYTHON_EXECUTABLE:FILEPATH={:s}'.format(spec['python'].command.path))

        return args
