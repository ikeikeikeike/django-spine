from django import VERSION
from django.db import transaction
from django.conf import settings
from django.test import TestCase
from django.utils.functional import wraps

import pytest


def thetype(treetype, proxy):

    def decorator(f):

        @wraps(f)
        def _testtype(self):
            # tyreetype = MP, AL, NS
            getattr(self, 'set_' + treetype)(proxy)
            try:
                f(self)
            finally:
                transaction.rollback()
                self.model = None
                self.sorted_model = None
                self.dep_model = None
        return _testtype
    return decorator


def _load_test_methods(cls, proxy=True):
    if proxy:
        proxyopts = (False, True)
    else:
        proxyopts = (False,)
    for m in dir(cls):
        if not m.startswith('_multi_'):
            continue
        for t in ('MP', 'AL', 'NS'):
            for p in proxyopts:
                deco = thetype(t, p)
                if p:
                    _proxy = '_proxy'
                else:
                    _proxy = ''
                name = 'test_%s%s_%s' % (t.lower(),
                                          _proxy,
                                          m.split('_', 2)[2])
                test = deco(getattr(cls, m))

                # expected test failures
                if (
                        # Test class is TestDelete, and
                        cls.__name__ == 'TestDelete' and
                        # testing Materialized Path trees, and
                        t == 'MP' and
                        # testing proxy models, and
                        p and
                        # using Django is 1.3.X, and
                        VERSION[:2] == (1, 3) and
                        # database is MySQL
                        settings.DATABASES['default']['ENGINE'].endswith(
                            '.mysql')):
                    # If the above conditions are met, we expect this test to
                    # fail due to a bug in Django.
                    # See: Issue 44 in the bug tracker.
                    test = pytest.mark.xfail(test)

                setattr(cls, name, test)
        delattr(cls, m)


class TestSpineBase(TestCase):
    pass
