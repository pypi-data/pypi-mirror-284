import os

from parade.command import ParadeCommand


def check(tasks):
    non_deps_tasks = {}
    duplicate_tasks = {}
    circular_tasks = {}
    for task, deps in tasks.items():
        for dp in deps:
            # check for invalid dependencies
            if dp not in tasks:
                if task not in non_deps_tasks:
                    non_deps_tasks[task] = set()
                non_deps_tasks[task].add(dp)
            # check for duplicate dependencies
            if deps.count(dp) > 1:
                if task not in duplicate_tasks:
                    duplicate_tasks[task] = set()
                duplicate_tasks[task].add((dp, deps.count(dp)))
            # check for circular dependence
            if dp == task:
                if task not in circular_tasks:
                    circular_tasks[task] = list()
                circular_tasks[task].append(dp)
            if dp != task and dp in tasks and task in tasks[dp]:
                if task not in circular_tasks:
                    circular_tasks[task] = list()
                circular_tasks[task].append({dp: tasks[dp]})

    non_deps_tasks = {k: list(v) for k, v in non_deps_tasks.items()}
    duplicate_tasks = {k: list(v) for k, v in duplicate_tasks.items()}

    return non_deps_tasks, duplicate_tasks, circular_tasks


class CheckCommand(ParadeCommand):
    requires_workspace = True

    def run_internal(self, context, **kwargs):
        flow_name = kwargs.get('flow-name')
        env = kwargs.get("env")

        if env:
            os.environ["PARADE_PROFILE"] = env

        deps = {}
        if flow_name:
            flow_store = context.get_flowstore()
            flow = flow_store.load(flow_name)
            if flow:
                deps = {k: list(v) for k, v in flow.deps.items()}  # 依赖
                for task in flow.tasks:
                    if task not in deps:
                        deps[task] = []
        else:
            deps = dict([(task.name, list(task.deps)) for task in context.load_tasks().values()])

        non_deps, duplicate, circular = check(deps)

        print(f"Total: {len(deps)}")
        print('------------------------------------------')
        if len(non_deps) == 0 and len(duplicate) == 0 and len(circular) == 0:
            print('PASS')

        if len(non_deps) > 0:
            print('[Invalid Dependencies]')
            for k, v in non_deps.items():
                print(k, ' ==>  ', v)
            print('------------------------------------------')

        if len(duplicate) > 0:
            print('[Duplicate Dependencies]')
            for k, v in duplicate.items():
                print(k, ' ==>  ', v)
            print('------------------------------------------')

        if len(circular) > 0:
            print('[Circular Dependencies]')
            for k, v in circular.items():
                print(k, ' ==>  ', v)
            print('------------------------------------------')

    def config_parser(self, parser):
        parser.add_argument('--flow-name', nargs='?', help='the flow to check')
        parser.add_argument('-e', '--env', nargs='?', help='environment: default, prod, rc, dev')

    def short_desc(self):
        return 'check parade flow'
