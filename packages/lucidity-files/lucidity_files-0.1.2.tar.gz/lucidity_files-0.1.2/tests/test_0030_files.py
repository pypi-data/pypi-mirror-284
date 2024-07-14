'''
Created on Aug 28, 2021

@author: Eduardo Grana
'''
import unittest
import random
import inspect
import copy
import lucidity_files
import os

import test_helper

# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string


WHITELIST = []
# WHITELIST = ['0040']


class Test(unittest.TestCase):
    @unittest.skipIf((WHITELIST and '0010' not in WHITELIST), 'Whitelist is on for {} only '.format(WHITELIST))
    def test_0010_create(self):
        print('Starting test {}'.format(inspect.stack()[0][3]))

        template = test_helper.getTemplateByName('output_part_single_layer')
        print('\t', template.lucidity_name)

        root = test_helper.ROOT

        keys = [
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '001', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'ol', 'ext': 'ma', 'entity': '1020', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'final', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '002', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1020', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'ol', 'ext': 'ma', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '002', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'se2', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '001', 'step': 'art', 'layer': 'bg', 'ext': 'ma', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'model', 'name': 'test', 'XTDXrootout': root, 'publish': 'work', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'bg', 'ext': 'ma', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '001', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1020', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'se2', 'task': 'model', 'name': 'test', 'XTDXrootout': root, 'publish': 'work', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'ol', 'ext': 'ma', 'entity': '1030', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'se2', 'task': 'model', 'name': 'test', 'XTDXrootout': root, 'publish': 'work', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1020', 'entitytype': 'shot'},
        ]
        
        expected = [
            root + '/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_test_v001/bg/1010_art_anim_test_v001_bg.exr',
            root + '/testprj/shot/seq/1020/art/publish/anim/img/1020_art_anim_test_v003/ol/1020_art_anim_test_v003_ol.ma',
            root + '/testprj/shot/seq/1020/art/publish/anim/img/1020_art_anim_final_v002/bg/1020_art_anim_final_v002_bg.exr',
            root + '/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_test_v003/ol/1010_art_anim_test_v003_ol.ma',
            root + '/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_test_v002/bg/1010_art_anim_test_v002_bg.exr',
            root + '/testprj/shot/se2/1010/art/publish/anim/img/1010_art_anim_test_v001/bg/1010_art_anim_test_v001_bg.ma',
            root + '/testprj/shot/seq/1010/art/work/model/img/1010_art_model_test_v003/bg/1010_art_model_test_v003_bg.ma',
            root + '/testprj/shot/seq/1020/art/publish/anim/img/1020_art_anim_test_v001/bg/1020_art_anim_test_v001_bg.exr',
            root + '/testprj/shot/se2/1030/art/work/model/img/1030_art_model_test_v003/ol/1030_art_model_test_v003_ol.ma',
            root + '/testprj/shot/se2/1020/art/work/model/img/1020_art_model_test_v003/bg/1020_art_model_test_v003_bg.exr',
        ]

        # format and create files
        created_files = []
        for key, exp in zip(keys, expected):
            path = template.format(key)
            msg = 'Expected: {}\n\t got {}'.format(os.path.normpath(exp), path)
            self.assertEqual(path, os.path.normpath(exp), msg)
            test_helper.touch(path)
            created_files.append(path)

        # check they are listed and exists
        paths = template.getPaths(strict_check=True)
        print('\tfound {} paths'.format(len(paths)))
        for p in paths:
            # check only the ones we created
            if p not in expected:
                continue
            self.assertTrue(os.path.isfile(p), 'Could not find created path {}'.format(p))

        # cleanup
        for p in created_files:
            os.remove(p)

        print('Finished test {}'.format(inspect.stack()[0][3]))

    @unittest.skipIf((WHITELIST and '0020' not in WHITELIST), 'Whitelist is on for {} only '.format(WHITELIST))
    def test_0020_create_multi(self):
        print('Starting test {}'.format(inspect.stack()[0][3]))

        root = test_helper.ROOT

        expected = [
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v001/1010_art_model_final_v001_0001.ma",
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v001/1010_art_model_final_v001_0002.ma",
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v001/1010_art_model_final_v001_0003.ma",
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v002/1010_art_model_final_v002_0001.ma",
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v002/1010_art_model_final_v002_0002.ma",
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v002/1010_art_model_final_v002_0003.ma",
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v003/1010_art_model_final_v003_0001.ma",
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v003/1010_art_model_final_v003_0002.ma",
            root + "/testprj/shot/se2/1010/art/publish/model/img/1010_art_model_final_v003/1010_art_model_final_v003_0003.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v001/1010_art_anim_final_v001_0001.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v001/1010_art_anim_final_v001_0002.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v001/1010_art_anim_final_v001_0003.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v002/1010_art_anim_final_v002_0001.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v002/1010_art_anim_final_v002_0002.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v002/1010_art_anim_final_v002_0003.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v003/1010_art_anim_final_v003_0001.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v003/1010_art_anim_final_v003_0002.ma",
            root + "/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_final_v003/1010_art_anim_final_v003_0003.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v001/1020_art_anim_final_v001_0001.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v001/1020_art_anim_final_v001_0002.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v001/1020_art_anim_final_v001_0003.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v002/1020_art_anim_final_v002_0001.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v002/1020_art_anim_final_v002_0002.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v002/1020_art_anim_final_v002_0003.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v003/1020_art_anim_final_v003_0001.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v003/1020_art_anim_final_v003_0002.ma",
            root + "/testprj/shot/se2/1020/art/work/anim/img/1020_art_anim_final_v003/1020_art_anim_final_v003_0003.ma",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v001/1030_art_anim_test_v001_0001.exr",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v001/1030_art_anim_test_v001_0002.exr",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v001/1030_art_anim_test_v001_0003.exr",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v002/1030_art_anim_test_v002_0001.exr",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v002/1030_art_anim_test_v002_0002.exr",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v002/1030_art_anim_test_v002_0003.exr",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v003/1030_art_anim_test_v003_0001.exr",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v003/1030_art_anim_test_v003_0002.exr",
            root + "/testprj/shot/seq/1030/art/publish/anim/img/1030_art_anim_test_v003/1030_art_anim_test_v003_0003.exr",
        ]

        keys = [
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'model', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'model', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'model', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'model', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'model', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'model', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'model', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'model', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'model', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1010', 'entitytype': 'shot', 'ext': 'ma', 'group': 'seq', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1020', 'entitytype': 'shot', 'ext': 'ma', 'group': 'se2', 'name': 'final', 'outputtype': 'img', 'project': 'testprj', 'publish': 'work', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '001'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '002'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0001', 'step': 'art', 'task': 'anim', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0002', 'step': 'art', 'task': 'anim', 'version': '003'},
            {'XTDXrootout': root, 'entity': '1030', 'entitytype': 'shot', 'ext': 'exr', 'group': 'seq', 'name': 'test', 'outputtype': 'img', 'project': 'testprj', 'publish': 'publish', 'seq4': '0003', 'step': 'art', 'task': 'anim', 'version': '003'},
        ]

        template = test_helper.getTemplateByName('output_all_multi')
        print('\t', template.lucidity_name)
    
        # format and create files
        created_files = []
        for key, exp in zip(keys, expected):
            # print(template.parse(exp))
            path = template.format(key)
            msg = 'Expected: {}\n\t got {}'.format(os.path.normpath(exp), path)
            self.assertEqual(path, os.path.normpath(exp), msg)
            test_helper.touch(path)
            created_files.append(path)

        # check they are listed and exists
        paths = template.getPaths(strict_check=True)
        print('\tfound {} paths'.format(len(paths)))
        for p in paths:
            # check only the ones we created
            if p not in expected:
                continue
            self.assertTrue(os.path.isfile(p), 'Could not find created path {}'.format(p))

        # cleanup
        for p in created_files:
            os.remove(p)

        print('Finished test {}'.format(inspect.stack()[0][3]))

    @unittest.skipIf((WHITELIST and '0030' not in WHITELIST), 'Whitelist is on for {} only '.format(WHITELIST))
    def test_0030_list(self):
        print('Starting test {}'.format(inspect.stack()[0][3]))

        root = test_helper.ROOT

        pattern = '{XTDXrootout:[\\w_.\\-:]+}/{project}/{entitytype}/{group}/{entity}/{step}/{publish}/{task}/{outputtype}/{entity}_{step}_{task}_{name}_v{version}'
        pattern += '/{layer}/{entity}_{step}_{task}_{name}_v{version}_{layer}.{ext}'
        roots = {'XTDXrootout': root}


        template = lucidity_files.TemplateFile.create('test', pattern, roots=roots)

        keys = [
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '001', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'ol', 'ext': 'ma', 'entity': '1020', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'final', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '002', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1020', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'ol', 'ext': 'ma', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '002', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'se2', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '001', 'step': 'art', 'layer': 'bg', 'ext': 'ma', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'model', 'name': 'test', 'XTDXrootout': root, 'publish': 'work', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'bg', 'ext': 'ma', 'entity': '1010', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'seq', 'task': 'anim', 'name': 'test', 'XTDXrootout': root, 'publish': 'publish', 'project': 'testprj', 'version': '001', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1020', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'se2', 'task': 'model', 'name': 'test', 'XTDXrootout': root, 'publish': 'work', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'ol', 'ext': 'ma', 'entity': '1030', 'entitytype': 'shot'},
            {'outputtype': 'img', 'group': 'se2', 'task': 'model', 'name': 'test', 'XTDXrootout': root, 'publish': 'work', 'project': 'testprj', 'version': '003', 'step': 'art', 'layer': 'bg', 'ext': 'exr', 'entity': '1020', 'entitytype': 'shot'},
       ]
        
        expected = [
            root + '/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_test_v001/bg/1010_art_anim_test_v001_bg.exr',
            root + '/testprj/shot/seq/1020/art/publish/anim/img/1020_art_anim_test_v003/ol/1020_art_anim_test_v003_ol.ma',
            root + '/testprj/shot/seq/1020/art/publish/anim/img/1020_art_anim_final_v002/bg/1020_art_anim_final_v002_bg.exr',
            root + '/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_test_v003/ol/1010_art_anim_test_v003_ol.ma',
            root + '/testprj/shot/seq/1010/art/publish/anim/img/1010_art_anim_test_v002/bg/1010_art_anim_test_v002_bg.exr',
            root + '/testprj/shot/se2/1010/art/publish/anim/img/1010_art_anim_test_v001/bg/1010_art_anim_test_v001_bg.ma',
            root + '/testprj/shot/seq/1010/art/work/model/img/1010_art_model_test_v003/bg/1010_art_model_test_v003_bg.ma',
            root + '/testprj/shot/seq/1020/art/publish/anim/img/1020_art_anim_test_v001/bg/1020_art_anim_test_v001_bg.exr',
            root + '/testprj/shot/se2/1030/art/work/model/img/1030_art_model_test_v003/ol/1030_art_model_test_v003_ol.ma',
            root + '/testprj/shot/se2/1020/art/work/model/img/1020_art_model_test_v003/bg/1020_art_model_test_v003_bg.exr',
            ]

        # format and create files
        created_files = []
        for key, exp in zip(keys, expected):
            path = template.format(key)
            msg = 'Expected: {}\n\t got {}'.format(os.path.normpath(exp), path)
            self.assertEqual(path, os.path.normpath(exp), msg)
            test_helper.touch(path)
            created_files.append(path)

        # check they are listed and exists
        paths = template.getPaths(strict_check=True)
        print('\tfound {} paths'.format(len(paths)))
        for p in paths:
            # check only the ones we created
            if p not in expected:
                continue
            self.assertTrue(os.path.isfile(p), 'Could not find created path {}'.format(p))

        # cleanup
        for p in created_files:
            os.remove(p)

        print('Finished test {}'.format(inspect.stack()[0][3]))

    @unittest.skipIf((WHITELIST and '0040' not in WHITELIST), 'Whitelist is on for {} only '.format(WHITELIST))
    def test_040_partial_and_list(self):
        print('Starting test {}'.format(inspect.stack()[0][3]))

        # lets create a file to be listed
        # path = r"C:\test\asset\car\mod\hi\car_mod_hi_default_v001.txt"
        path = os.path.join(test_helper.ROOT, 'test/asset/car/mod/hi/car_mod_hi_default_v001.txt')

        if not os.path.isfile(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w'):
                pass

        roots = {'root': test_helper.ROOT}

        # define a relative path from the root
        pattern = '{root:[\w_.\-:]+}/{project}/{entitytype}/{entity}/{step}/{task}/{entity}_{step}_{task}_{name}_v{version}.{ext}'
        lf_template = lucidity_files.TemplateFile.create('assets', pattern, roots=roots)

        # lets get a partial template to the entity folder
        partial_template = lf_template.getPartialTemplateFile('entity')

        # list all entity folders
        paths_found = partial_template.getPaths({'project': 'test'}, strict_check=True)
        self.assertTrue(paths_found, 'Could not find expected path! {}'.format(path))

        # now get each path's data
        for path in paths_found:
            print('\t', path)
            data = partial_template.parse(path)
            print('\t', data)

        if os.path.isfile(path):
            os.remove(path)

        print('Finished test {}'.format(inspect.stack()[0][3]))


if __name__ == "__main__":
    unittest.main()
