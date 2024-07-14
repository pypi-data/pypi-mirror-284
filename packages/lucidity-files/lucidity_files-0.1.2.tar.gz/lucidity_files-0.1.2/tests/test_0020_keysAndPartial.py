'''
Created on Aug 28, 2021

@author: Eduardo Grana
'''
import inspect
import shutil
import unittest
import os

import test_helper

WHITELIST = []
# WHITELIST = ['0030']

# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string


class Test(unittest.TestCase):
    @unittest.skipIf((WHITELIST and '0010' not in WHITELIST), 'Whitelist is on for {} only '.format(WHITELIST))
    def test_0010_orderedTokens(self):
        print('Starting test {}'.format(inspect.stack()[0][3]))

        template = test_helper.getTemplateByName('output_part_single_layer')
        r = template._getOrderedKeyTokens(template.l_template.pattern)

        expected = [
            'XTDXrootout',
            'project',
            'entitytype',
            'group',
            'entity',
            'step',
            'publish',
            'task',
            'outputtype',
            'name',
            'version',
            'layer',
            'ext',
        ]
        msg = 'Expected {} and got {}'.format(expected, r)
        self.assertEqual(r, expected, msg)

        print('\tGot', r, 'OK')

        print('Finished test {}'.format(inspect.stack()[0][3]))

    @unittest.skipIf((WHITELIST and '0015' not in WHITELIST), 'Whitelist is on for {} only '.format(WHITELIST))
    def test_0015_orderedTokens(self):
        print('Starting test {}'.format(inspect.stack()[0][3]))

        template = test_helper.getTemplateByName('output_part_single_layer')
        r = template.getKeys(ordered=True)

        expected = [
            'project',
            'entitytype',
            'group',
            'entity',
            'step',
            'publish',
            'task',
            'outputtype',
            'name',
            'version',
            'layer',
            'ext',
        ]
        msg = 'Expected {} and got {}'.format(expected, r)
        self.assertEqual(r, expected, msg)

        print('\tGot', r, 'OK')

        print('Finished test {}'.format(inspect.stack()[0][3]))

    @unittest.skipIf((WHITELIST and '0020' not in WHITELIST), 'Whitelist is on for {} only '.format(WHITELIST))
    def test_0020_partialPattern(self):
        print('Starting test {}'.format(inspect.stack()[0][3]))

        template = test_helper.getTemplateByName('output_part_single_layer')
        r = template._getPartialPattern('entity')

        expected = '{XTDXrootout:[\\w_.\\-:]+}/{project}/{entitytype}/{group}/{entity}'

        msg = 'Expected {} and got {}'.format(expected, r)
        self.assertEqual(r, expected, msg)

        print('\tGot', r, 'OK')

        print('Finished test {}'.format(inspect.stack()[0][3]))

    @unittest.skipIf((WHITELIST and '0030' not in WHITELIST), 'Whitelist is on for {} only '.format(WHITELIST))
    def test_0030_partialPattern(self):
        print('Starting test {}'.format(inspect.stack()[0][3]))

        template = test_helper.getTemplateByName('output_part_single_layer')

        root = test_helper.ROOT
        lucidity_style_root = root.replace('\\', '/')

        if os.path.isdir(root):
            shutil.rmtree(root,ignore_errors=True)

        template_file = template.getPartialTemplateFile('entity')

        os.makedirs(root, exist_ok=True)

        expected_paths = sorted([
            os.path.join(root, 'testprj', 'shot', 'se2', '1010'),
            os.path.join(root, 'testprj', 'shot', 'se2', '1020'),
            os.path.join(root, 'testprj', 'shot', 'se2', '1030'),
            os.path.join(root, 'testprj', 'shot', 'seq', '1010'),
            os.path.join(root, 'testprj', 'shot', 'seq', '1020'),
            os.path.join(root, 'testprj', 'shot', 'seq', '1030'),
        ])
        keys = [
                {
                    'project': 'testprj',
                    'group': 'se2',
                    'XTDXrootout': lucidity_style_root,
                    'entitytype': 'shot',
                    'entity': '1010',
                },
                {
                    'project': 'testprj',
                    'group': 'se2',
                    'XTDXrootout': lucidity_style_root,
                    'entitytype': 'shot',
                    'entity': '1020',
                },
                {
                    'project': 'testprj',
                    'group': 'se2',
                    'XTDXrootout': lucidity_style_root,
                    'entitytype': 'shot',
                    'entity': '1030',
                },
                {
                    'project': 'testprj',
                    'group': 'seq',
                    'XTDXrootout': lucidity_style_root,
                    'entitytype': 'shot',
                    'entity': '1010',
                },
                {
                    'project': 'testprj',
                    'group': 'seq',
                    'XTDXrootout': lucidity_style_root,
                    'entitytype': 'shot',
                    'entity': '1020',
                },
                {
                    'project': 'testprj',
                    'group': 'seq',
                    'XTDXrootout': lucidity_style_root,
                    'entitytype': 'shot',
                    'entity': '1030',
                },
        ]

        # create paths
        created_folders = []
        for key in keys:
            p = template_file.format(key)
            test_helper.mkdir(p)
            created_folders.append(p)

        paths = sorted(template_file.getPaths())
        datas = [template_file.parse(p) for p in paths]

        msg = 'Expected {} and got {}'.format(expected_paths, paths)
        self.assertEqual(expected_paths, paths, msg)
        msg = 'Expected {} and got {}'.format(keys, datas)
        self.assertEqual(keys, datas, msg)

        for o in created_folders:
            shutil.rmtree(o, ignore_errors=True)

        print('Finished test {}'.format(inspect.stack()[0][3]))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
