import mitogen
import mitogen.utils

def hello_world():
    return "Hello World"


def run_remote_hello(hostname, username):
    def router_func(router):
        ssh_context = router.ssh(
            hostname=hostname,
            username=username,
        )
        return ssh_context.call(hello_world)

    return mitogen.utils.with_router(router_func)  # Actually calls router_func with the router


if __name__ == '__main__':
    result = run_remote_hello('test', 'root')
    print(result)
