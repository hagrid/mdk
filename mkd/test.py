import mitogen
import mitogen.utils


def get_time():
    import time
    return time.time()


def run_remote_function():
    router = mitogen.master.Router()
    try:
        context = router.ssh(
            hostname='test',
            username='root',
            python_path='python3',
            # password='xxx'
        )

        result = context.call(get_time)
        print("Remote time:", result)
    finally:
        router.disconnect(context)


if __name__ == '__main__':
    run_remote_function()
