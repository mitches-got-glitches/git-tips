from operator import itemgetter

from tree_format import format_tree

tree = (
    'repo', [
        ('package_name', [
            ('sub_package', [
                ('scrumptious_module.py', []),
            ]),
            ('tasty_module.py', []),
            ('delicious_module.py', []),
        ]),
        ('test', [
            ('sub_package', [
                ('test_scrumptious_module.py', []),
            ]),
            ('test_tasty_module.py', []),
            ('test_delicious_module.py', []),
        ]),
    ],
)

print(format_tree(tree, format_node=itemgetter(0), get_children=itemgetter(1)))