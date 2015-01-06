from fabric.api import *
env.user = 'root'
env.hosts = ['61.152.73.222']
env.password = '9Jl1Dwo+Ub'


def pack():
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/{}.tar.gz'.format(dist), '/tmp/hc_test.tar.gz')
    run('sudo rm -rf /tmp/hc_test_src')
    run('sudo mkdir /tmp/hc_test_src')
    with cd('/tmp/hc_test_src'):
        run('sudo tar xzf /tmp/hc_test.tar.gz')
    run('sudo rm -rf /root/Documents/hc_test')
    run('sudo cp -r /tmp/hc_test_src/{} /root/Documents/hc_test'.format(dist))
    run('sudo rm -rf /tmp/hc_test_src')


def runtest():
    with cd('/root/Documents/hc_test/'):
        run('. run.sh')


def getreport():
    with cd('/root/Documents/hc_test/test'):
        get('report','/tmp/')



def all():
    pack()
    deploy()
    runtest()
    getreport()
